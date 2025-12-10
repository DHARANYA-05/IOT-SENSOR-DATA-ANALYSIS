# IoT Sensor Data Analysis — PySpark + Flask + Pandas

**Project Title:** Analyze real-time IoT data from multiple sensors to detect faults or anomalies.

**Problem Statement:** Industrial automation and predictive maintenance — detect sensor failures and abnormal activity from logs.

**Use Case:** Sensor logs (CSV). This demo loads a synthetic dataset with 100k+ records.

**Expected Output:** Alerts for sensor failures (anomalies detected via 3-sigma rule), summary statistics, time-series charts.

## Overview

- **Frontend:** Interactive dashboard (HTML/CSS/JS) with time-series charts, statistics, and anomaly alerts.
- **Backend:** Flask REST API (pandas or PySpark).
- **Data:** CSV datasets in `data/` folder (large dataset generator included).
- **Anomaly Detection:** Statistical 3-sigma rule per sensor (flags values > mean ± 3*stddev).

## Quick Start (One Command)

Run this from the project root in PowerShell:

```powershell
.\run_all.ps1
```

This script will:
1. Create a Python virtual environment (venv).
2. Install Flask and pandas (fast, no heavy dependencies).
3. Generate the large dataset if missing (100k sensor records).
4. Start the Flask server (http://127.0.0.1:8080).
5. Open Chrome to the dashboard.

**That's it!** The page will appear in Chrome automatically. No manual steps needed.

---

## Manual Setup (If You Prefer)

If you want to run the steps yourself:

### 1. Create and Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
.\.venv\Scripts\pip.exe install Flask pandas
```

Optional: For PySpark support (requires download):

```powershell
.\.venv\Scripts\pip.exe install pyspark
```

### 3. Generate a Large Dataset (Optional)

```powershell
.\.venv\Scripts\python.exe .\data\generate_dataset.py --rows 100000 --sensors 200 --out sensor_data_100k.csv
```

### 4. Start the Server

```powershell
.\.venv\Scripts\python.exe .\app\main.py
```

### 5. Open in Chrome

```powershell
Start-Process "chrome.exe" "http://127.0.0.1:8080"
```

---

## Understanding the Project

### Backend Architecture

- **Flask** (`app/main.py`): REST API endpoints for data retrieval and anomaly detection.
- **SparkService** (`app/spark_service.py`): 
  - Uses **pandas** by default (fast, no dependencies).
  - Automatically switches to **PySpark** if installed (for Spark UI and large-scale jobs).
  - Both implementations have the same API: `load_csv()`, `summary_json()`, `detect_anomalies()`.

### Frontend

- **Dashboard** (`app/templates/index.html`): Shows charts, statistics, anomalies, and dataset selector.
- **Styles** (`app/static/styles.css`): Modern Bootstrap-based UI.
- **Scripts** (`app/static/app.js`): Fetches data via REST endpoints, renders charts using Chart.js.

### Anomaly Detection

**Algorithm:** 3-Sigma Rule
- For each sensor, calculate: mean (μ) and standard deviation (σ).
- Flag any reading where `|value - μ| > 3*σ`.
- This catches ~99.7% of abnormal values in normal data distribution.

### REST Endpoints

| Endpoint          | Method | Purpose |
|-------------------|--------|---------|
| `/`               | GET    | Dashboard page |
| `/data`           | GET    | All sensor data as JSON |
| `/summary`        | GET    | Statistical summary (count, mean, std, min, max) |
| `/anomalies`      | GET    | Detected anomalies |
| `/datasets`       | GET    | List available CSV files |
| `/set_dataset`    | POST   | Switch to a different CSV |
| `/info`           | GET    | Runtime info (backend type, dataset path, row count) |
| `/health`         | GET    | Health check |

### Dataset Format

CSV with columns: `sensor_id, timestamp, value, status`

Example:
```
sensor_001,2025-11-04T00:00:00,23.5,normal
sensor_001,2025-11-04T00:01:00,23.7,normal
sensor_001,2025-11-04T00:02:00,98.2,fault
```

---

## Troubleshooting

### "Proxy/Firewall Error"

The app binds to `127.0.0.1` (localhost only) to avoid external firewall interception. This should work on any Windows machine without admin changes.

If pip fails to download packages due to proxy:
```powershell
$env:HTTP_PROXY = 'http://proxy.example.com:3128'
$env:HTTPS_PROXY = 'http://proxy.example.com:3128'
```

Then retry the pip install.

### "No module named 'pyspark'"

This is OK. The app automatically uses pandas instead (faster, no dependencies). Pandas is already installed.

If you want PySpark (optional):
```powershell
.\.venv\Scripts\pip.exe install pyspark
```

### "Chrome didn't open"

Open manually:
```powershell
Start-Process "chrome.exe" "http://127.0.0.1:8080"
```

### "Server won't start"

Check for port conflicts:
```powershell
netstat -ano | findstr :8080
```

If port 8080 is in use, stop the process or set a different port:
```powershell
$env:PORT = 9090
.\.venv\Scripts\python.exe .\app\main.py
```

Then open: `http://127.0.0.1:9090`

---

## Advanced: Generate Larger Datasets

To test performance with larger datasets:

```powershell
.\.venv\Scripts\python.exe .\data\generate_dataset.py --rows 1000000 --sensors 500 --out sensor_data_1m.csv
```

Then in the dashboard, use the dataset selector dropdown to switch to the new file.

---

## Notes

- **Backend:** Defaults to pandas. If pyspark is installed, uses PySpark (no code changes needed).
- **Spark UI:** If using PySpark, Spark Web UI is available at `http://localhost:4040/` (job monitoring, DAG visualization, etc.).
- **Performance:** Pandas handles 100k+ rows smoothly. For 1M+ rows, use PySpark (requires installation).
- **Production:** This is a demo. For production use, deploy on a WSGI server (Gunicorn, etc.) and secure the endpoints.

---

## What's Included

```
c:\spark project\
├── app/
│   ├── main.py                 # Flask backend (REST endpoints)
│   ├── spark_service.py        # Spark/pandas service
│   ├── templates/
│   │   └── index.html          # Dashboard UI
│   └── static/
│       ├── app.js              # Frontend logic
│       └── styles.css          # Dashboard styling
├── data/
│   ├── sensor_data.csv         # Small sample
│   ├── sensor_data_100k.csv    # Generated (100k rows)
│   └── generate_dataset.py     # Dataset generator script
├── requirements.txt            # Python dependencies
├── run_all.ps1                 # One-click startup script
└── README.md                   # This file
```

---

## Next Steps

1. **Explore the UI:** Open the dashboard, switch datasets, check anomalies.
2. **Generate More Data:** Use `generate_dataset.py --rows 500000` to test larger datasets.
3. **Enable PySpark:** Install pyspark and view Spark UI for advanced job monitoring.
4. **Customize:** Modify `spark_service.py` to add different anomaly detection algorithms (isolation forest, LOF, etc.).
5. **Deploy:** Containerize with Docker or deploy to a cloud platform (Azure, AWS, GCP).

---

**Questions?** Check server logs (printed in terminal) or browser console (F12) for debugging info.
