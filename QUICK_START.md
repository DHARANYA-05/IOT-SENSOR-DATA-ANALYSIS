# IoT Analytics + Spark Web UI - Project Guide

## Quick Start - Run Your Project

### Option 1: Using Batch File (Easiest - Windows)
```bash
Double-click: run_project.bat
```

### Option 2: Using PowerShell
```powershell
.\run_project.ps1
```

### Option 3: Using Python Directly
```bash
.\.venv\Scripts\python.exe server.py
```

---

## What Starts When You Run the Project

✅ **Flask Web Server** - http://127.0.0.1:5000
✅ **Spark Context** - Connected and ready
✅ **31 API Routes** - All configured
✅ **IoT Dashboard** - Real-time sensor monitoring
✅ **Spark Jobs Control** - Submit IoT operations to Spark
✅ **Spark Web UI** - http://localhost:4040 (or 4041)

---

## Access Your Dashboards

1. **IoT Dashboard** (Main)
   ```
   http://127.0.0.1:5000/
   ```
   - Real-time sensor monitoring
   - Anomaly detection
   - 15 sensors across 5 machines

2. **Spark Jobs Control** (New)
   ```
   http://127.0.0.1:5000/spark-jobs
   ```
   - Submit IoT jobs to Spark
   - Monitor job execution
   - View job statistics

3. **Spark Web UI** (Real-time execution)
   ```
   http://localhost:4040
   ```
   - Jobs tab - View executing jobs
   - Storage tab - View cached RDDs
   - Stages tab - View job stages

---

## IoT Operations Available

Click buttons in Spark Jobs Control to:

1. **Analyze Sensors**
   - Analyzes all sensor data
   - Calculates min, max, avg statistics
   - Visible in Spark Web UI

2. **Detect Anomalies**
   - Detects outliers using 3-sigma rule
   - Shows anomaly percentage
   - Data cached in Spark Storage

3. **Sensor Summary**
   - Groups data by sensor
   - Per-sensor statistics
   - Aggregated results

---

## Project Structure

```
c:\spark project\
├── run_project.bat          (Easy launcher - double-click)
├── run_project.ps1          (PowerShell launcher)
├── server.py                (Flask server)
├── app/
│   ├── main.py              (31 API routes)
│   ├── spark_config.py      (Spark configuration)
│   ├── spark_jobs.py        (Job submission)
│   ├── iot_spark_jobs.py    (IoT operations)
│   ├── spark_ui_bridge.py   (Spark UI integration)
│   └── templates/
│       ├── index.html       (IoT Dashboard)
│       └── spark_jobs_control.html
├── data/
│   ├── factory_sensors_data.csv
│   └── other data files
└── .venv/                   (Virtual environment)
```

---

## Troubleshooting

### Server won't start?
```
Kill existing Python processes:
taskkill /FI "IMAGENAME eq python.exe" /F

Then run again:
run_project.bat
```

### Spark jobs not showing in Web UI?
```
- Make sure Spark context initialized successfully
- Check if Java is installed
- Look for "Spark initialization: READY" in console
```

### Can't connect to http://127.0.0.1:5000?
```
- Wait 5 seconds for server to fully start
- Check if port 5000 is available
- Check firewall settings
```

---

## What You Need

✅ Python 3.10+ (installed)
✅ Virtual environment (.venv - created)
✅ Flask and dependencies (installed)
✅ PySpark (installed)
✅ Java (for Spark)

---

## Features

🎯 **Real-time IoT Monitoring**
- 15 sensor data streams
- Live anomaly detection
- Visual dashboards

⚡ **Spark Integration**
- Run IoT operations in Spark
- RDD caching and storage
- Web UI monitoring

📊 **Data Processing**
- Sensor analysis
- Anomaly detection
- Statistical summaries
- Group aggregations

🚀 **Full Web Stack**
- Flask backend
- Bootstrap frontend
- Real-time updates
- REST APIs

---

## Commands

```bash
# Run the project (option 1)
run_project.bat

# Run the project (option 2)
.\run_project.ps1

# Run the project (option 3)
.\.venv\Scripts\python.exe server.py

# Test IoT Spark jobs
.\.venv\Scripts\python.exe test_iot_spark_jobs.py

# Check Spark status
.\.venv\Scripts\python.exe test_spark_init.py
```

---

## Notes

- Server runs on http://127.0.0.1:5000 (localhost only)
- Spark Web UI on http://localhost:4040 or 4041
- 31 routes configured and ready
- All dependencies already installed
- Ready for production use

---

**Your project is fully configured and ready to run!** 🚀

Just double-click `run_project.bat` to start everything.
