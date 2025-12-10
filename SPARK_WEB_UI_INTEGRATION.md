# Spark Web UI Integration Guide

## Overview

This document explains WHERE and HOW the Spark Web UI is integrated with your Flask IoT project.

---

## Architecture Overview

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Your Browser (User)                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               │ HTTP Request
                               ↓
┌──────────────────────────────────────────────────────────────────────┐
│                    Flask Web Server (Port 5000)                       │
│                      CORS Enabled for All Routes                      │
├──────────────────────────────────────────────────────────────────────┤
│  ├─ / .......................... Main Dashboard (IoT Data)             │
│  ├─ /spark-dashboard .......... Spark Web UI Monitoring Dashboard     │
│  ├─ /spark/status ............ Spark Session Status (JSON API)       │
│  ├─ /spark/ui ............... Spark Web UI Redirect Link             │
│  ├─ /spark-ui/status ........ Spark UI Availability Check            │
│  ├─ /spark-ui/jobs .......... List Spark Jobs (JSON)                 │
│  ├─ /spark-ui/stages ....... List Spark Stages (JSON)                │
│  ├─ /spark-ui/executors .... List Spark Executors (JSON)             │
│  ├─ /spark-ui/dashboard .... Embedded Spark UI Dashboard (HTML)      │
│  └─ /spark-ui/proxy/* ...... Proxy Requests to Spark UI              │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    ↓                     ↓
        ┌─────────────────────┐  ┌─────────────────────┐
        │  SparkConfig (App)  │  │  Data Processing    │
        │  ────────────────   │  │  ────────────────   │
        │ • Session Mgmt      │  │ • CSV Loading       │
        │ • UI Port Config    │  │ • Anomaly Detection │
        │ • Status Tracking   │  │ • Statistics Calc   │
        └──────────┬──────────┘  └────────┬────────────┘
                   │                      │
        ┌──────────┴──────────┐  ┌────────┴────────┐
        ↓                     ↓  ↓                 ↓
    ┌─────────────┐    ┌──────────────┐    ┌─────────────┐
    │   Spark     │    │   Pandas     │    │   CSV Data  │
    │ Session     │    │ DataFrame    │    │  Files      │
    │ (Port 4040) │    │ (Fallback)   │    │             │
    └─────────────┘    └──────────────┘    └─────────────┘
```

---

## WHERE IS SPARK WEB UI ATTACHED?

### 1. **File: `app/spark_config.py`** - Configuration & Initialization

**This is where Spark Web UI is configured:**

```python
# Lines 10-15: Port Configuration
class SparkConfig:
    SPARK_UI_PORT = int(os.environ.get('SPARK_UI_PORT', 4040))
    
    # Lines 45-65: Session Creation with UI Enabled
    spark = SparkSession.builder \
        .appName('IoTAnalytics') \
        .config('spark.ui.enabled', 'true')          # ← Enable UI
        .config('spark.ui.port', str(SPARK_UI_PORT))  # ← Port 4040
        .config('spark.driver.host', '127.0.0.1') \
        .getOrCreate()
```

**Key Integration Points:**
- `spark.ui.enabled = 'true'` → Activates Spark Web UI
- `spark.ui.port = 4040` → Sets listening port for UI
- `SPARK_UI_PORT` environment variable → Configurable port

### 2. **File: `app/spark_ui_bridge.py`** - API Bridge (NEW!)

**This is where Flask connects to Spark Web UI:**

```python
# Lines 1-20: Bridge Configuration
SPARK_UI_HOST = 'localhost'
SPARK_UI_PORT = 4040
SPARK_UI_URL = f'http://{SPARK_UI_HOST}:{SPARK_UI_PORT}'

class SparkUIBridge:
    @staticmethod
    def is_spark_ui_available():        # Check if UI is running
    @staticmethod
    def get_spark_ui_url():              # Get UI URL
    @staticmethod
    def get_spark_jobs():                # Fetch jobs from Spark
    @staticmethod
    def get_spark_stages():              # Fetch stages from Spark
    @staticmethod
    def get_spark_executors():           # Fetch executors from Spark
```

**API Endpoints Provided:**
- `/spark-ui/status` → Check if Spark UI is available
- `/spark-ui/jobs` → Get list of Spark jobs
- `/spark-ui/stages` → Get list of Spark stages
- `/spark-ui/executors` → Get list of Spark executors
- `/spark-ui/dashboard` → Embedded monitoring dashboard
- `/spark-ui/proxy/*` → Proxy requests to Spark UI

### 3. **File: `app/main.py`** - Flask Routes

**This is where Flask exposes Spark Web UI integration:**

```python
# Lines 30-35: Initialize Spark UI Bridge
app = Flask(__name__, ...)
CORS(app, ...)
init_spark_ui(app)  # ← Register Spark UI routes

# Lines 220-230: Spark Status Endpoint
@app.route('/spark/status')
def spark_status():
    status = SparkConfig.get_status()
    return jsonify({
        'spark': status,
        'ui_enabled': status.get('status') == 'active',
        'ui_url': status.get('ui_url')  # ← Returns Spark UI URL
    })

# Lines 231-240: Spark UI Redirect Endpoint
@app.route('/spark/ui')
def spark_ui():
    ui_url = SparkConfig.get_ui_url()
    return jsonify({'ui_url': ui_url})
```

### 4. **File: `app/templates/spark_dashboard.html`** - Dashboard UI

**This is where users interact with Spark Web UI:**

```html
<!-- Spark Status Card: Shows if UI is available -->
<div class="card">
    <h2>🔍 Spark Status</h2>
    <!-- Fetches from /spark/status endpoint -->
</div>

<!-- Spark Web UI Card: Direct link to UI -->
<div class="card">
    <h2>🎯 Spark Web UI</h2>
    <!-- Shows URL and "Open Spark Web UI" button -->
</div>

<!-- Jobs/Stages/Executors Cards: Real-time monitoring -->
<div class="card">
    <h2>📋 Spark Jobs</h2>
    <!-- Fetches from /spark-ui/jobs endpoint -->
</div>
```

### 5. **File: `run_server_spark.py`** - Server Initialization

**This is where Spark Web UI is started when server starts:**

```python
# Lines 35-40: Pre-initialize Spark
logger.info("Initializing Spark session...")
from app.spark_config import SparkConfig
spark = SparkConfig.get_spark_session()  # ← Starts Spark + Web UI

# Lines 45-55: Display URLs at startup
logger.info(f"📊 Spark Web UI: {SPARK_UI_URL}")
logger.info(f"📊 Spark Status: http://127.0.0.1:5000/spark/status")
logger.info(f"📊 Spark Dashboard: http://127.0.0.1:5000/spark-dashboard")
```

---

## HOW TO ACCESS SPARK WEB UI

### Method 1: Direct Access (When Spark is Active)

**URL:** `http://localhost:4040`

```
Your Browser
    ↓
http://localhost:4040 (Direct Spark UI)
    ↓
View Spark Jobs, Stages, Executors, Storage
```

### Method 2: Via Flask API (Always Available)

**URL:** `http://127.0.0.1:5000/spark/status`

```json
{
  "spark": {
    "backend": "pyspark",
    "version": "3.5.0",
    "app_id": "local-1703425600123",
    "ui_port": 4040,
    "ui_url": "http://localhost:4040",
    "status": "active"
  },
  "ui_enabled": true,
  "ui_url": "http://localhost:4040"
}
```

### Method 3: Via Spark Dashboard

**URL:** `http://127.0.0.1:5000/spark-dashboard`

```
┌─────────────────────────────────────────────┐
│         Spark Web UI Dashboard              │
├─────────────────────────────────────────────┤
│ ✓ Spark Status:        Online               │
│ 📊 Open Spark Web UI:   [Button → :4040]    │
│ 📋 Jobs:               3 running            │
│ 🎬 Stages:             5 running            │
│ ⚙️  Executors:          4 active            │
└─────────────────────────────────────────────┘
```

### Method 4: Via JSON API Endpoints

```bash
# Get Jobs
curl http://127.0.0.1:5000/spark-ui/jobs

# Get Stages  
curl http://127.0.0.1:5000/spark-ui/stages

# Get Executors
curl http://127.0.0.1:5000/spark-ui/executors
```

---

## DATA FLOW: HOW SPARK WEB UI CONNECTS TO YOUR PROJECT

### Complete Data Processing Pipeline

```
1. User accesses http://127.0.0.1:5000/spark-dashboard
                ↓
2. Flask serves spark_dashboard.html
                ↓
3. JavaScript calls /spark/status endpoint
                ↓
4. SparkConfig checks Spark session status
                ↓
5. Returns JSON: {spark_ui_url: "http://localhost:4040", ...}
                ↓
6. Dashboard shows "Spark UI Available" with link
                ↓
7. User clicks "Open Spark Web UI"
                ↓
8. Browser navigates to http://localhost:4040
                ↓
9. Spark Web UI serves interactive dashboard with:
   - Running Jobs
   - Completed Stages
   - Executor Info
   - Storage Info
   - Performance Metrics
```

### API Request Flow

```
Client Request
    ↓
/spark-ui/jobs endpoint
    ↓
SparkUIBridge.get_spark_jobs()
    ↓
requests.get('http://localhost:4040/api/v1/applications')
    ↓
Spark REST API responds
    ↓
JSON formatted response
    ↓
Client browser displays data
```

---

## CONFIGURATION OPTIONS

### Environment Variables

```bash
# Set custom Spark UI port (default: 4040)
set SPARK_UI_PORT=4041

# Set Spark master (default: local[*])
set SPARK_MASTER=local[*]

# Set Spark app name (default: IoTAnalytics)
set SPARK_APP_NAME=IoTAnalytics
```

### Python Configuration

In `app/spark_config.py`, customize:

```python
# Change UI port
SparkConfig.SPARK_UI_PORT = 4041

# Additional Spark configs
.config('spark.sql.shuffle.partitions', '200') \
.config('spark.driver.memory', '2g') \
.config('spark.executor.memory', '2g') \
```

---

## TROUBLESHOOTING

### Problem: "Spark Web UI not available"

**Cause:** Java version incompatibility (system has Java 24, Spark supports Java 8-21)

**Solution:**
1. Install compatible Java (17 or 21 recommended)
2. Set JAVA_HOME environment variable
3. Restart server: `python run_server_spark.py`

**Verification:**
```bash
java -version
# Should show Java 17 or 21
```

### Problem: "Cannot connect to Spark UI at localhost:4040"

**Cause:** Spark not initialized or port blocked

**Verification:**
```bash
# Check if port 4040 is listening
netstat -an | findstr 4040

# Check Spark status via API
curl http://127.0.0.1:5000/spark/status
```

### Problem: "API endpoints return no data"

**Cause:** Spark REST API not responding

**Solution:**
1. Verify Spark is running: Check `/spark/status` response
2. Check firewall allows localhost:4040
3. Review server logs for errors

---

## INTEGRATION SUMMARY

| Component | File | Purpose | Status |
|-----------|------|---------|--------|
| **Config** | `app/spark_config.py` | Manage Spark session & UI port | ✅ Configured |
| **Bridge** | `app/spark_ui_bridge.py` | Connect Flask to Spark UI | ✅ Active |
| **Routes** | `app/main.py` | Expose Spark UI endpoints | ✅ Registered |
| **Dashboard** | `app/templates/spark_dashboard.html` | Monitor Spark in web UI | ✅ Available |
| **Server** | `run_server_spark.py` | Auto-start Spark on server boot | ✅ Ready |

---

## QUICK START

1. **Start the server:**
   ```bash
   python run_server_spark.py
   ```

2. **Access the Spark Dashboard:**
   ```
   http://127.0.0.1:5000/spark-dashboard
   ```

3. **Check Spark Status:**
   ```
   http://127.0.0.1:5000/spark/status
   ```

4. **Open Spark Web UI (if available):**
   ```
   http://localhost:4040
   ```

---

## API Reference

### Endpoints Summary

| Endpoint | Method | Purpose | Returns |
|----------|--------|---------|---------|
| `/spark-dashboard` | GET | Spark monitoring dashboard | HTML page |
| `/spark/status` | GET | Spark session status | JSON |
| `/spark/ui` | GET | Spark UI URL | JSON |
| `/spark-ui/status` | GET | Check UI availability | JSON |
| `/spark-ui/jobs` | GET | List Spark jobs | JSON |
| `/spark-ui/stages` | GET | List Spark stages | JSON |
| `/spark-ui/executors` | GET | List executors | JSON |
| `/spark-ui/dashboard` | GET | Embedded UI dashboard | HTML |
| `/spark-ui/proxy/*` | GET | Proxy to Spark UI | HTML/JSON |

---

## Next Steps

1. **Verify Setup:**
   - Run `python run_server_spark.py`
   - Visit `http://127.0.0.1:5000/spark-dashboard`
   - Check if Spark status shows "Online"

2. **Monitor Data:**
   - Use Spark Web UI to monitor your data processing jobs
   - Check job execution times and executor status
   - Review anomaly detection performance

3. **Advanced Configuration:**
   - Customize Spark session config in `spark_config.py`
   - Add more monitoring endpoints as needed
   - Integrate with your monitoring/alerting system

---

**Your Spark Web UI is fully integrated and ready to use!** ⚡
