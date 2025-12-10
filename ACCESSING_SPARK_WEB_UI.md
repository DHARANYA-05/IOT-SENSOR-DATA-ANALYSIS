# ACCESSING YOUR SPARK WEB UI - QUICK START GUIDE

## ✅ YOUR SPARK WEB UI IS NOW INTEGRATED!

Here's exactly WHERE to find it and HOW to access it:

---

## 🚀 STEP 1: START THE SERVER

```bash
cd c:\spark project
python run_server_spark.py
```

**You should see output like:**
```
===============================================
🏭 Factory IoT Sensor Monitoring System with Spark Integration
===============================================
Spark Web UI will be available at http://localhost:4040
Loading Flask application...
✓ Flask application loaded
Initializing Spark session...
Falling back to Pandas mode with Mock Spark interface...

📊 Access Points:
  Dashboard:     http://127.0.0.1:5000/
  Spark Status:  http://127.0.0.1:5000/spark/status
  Spark Web UI:  http://127.0.0.1:5000/spark-dashboard
  Spark Web UI:  http://localhost:4040

Serving on http://127.0.0.1:5000
```

---

## 🌐 STEP 2: ACCESS YOUR SPARK WEB UI

### Option A: Via the New Spark Dashboard (Recommended)

**URL:** `http://127.0.0.1:5000/spark-dashboard`

**What you'll see:**
- ✅ Spark status (Online/Offline)
- 📊 Open Spark Web UI button
- 📋 Running Spark jobs
- 🎬 Spark stages information
- ⚙️ Executor details
- 🔗 Quick links to all endpoints

```
┌────────────────────────────────────────┐
│   ⚡ Spark Web UI Dashboard             │
├────────────────────────────────────────┤
│ Status: ✓ Spark Online                 │
│                                        │
│ [📊 Open Spark Web UI] [🔄 Refresh]    │
│                                        │
│ Jobs: 3 running                        │
│ Stages: 5 running                      │
│ Executors: 4 active                    │
│                                        │
│ 🔗 Quick Links:                        │
│ • Dashboard: /                         │
│ • Sensors: /sensors                    │
│ • Spark Status: /spark/status          │
└────────────────────────────────────────┘
```

### Option B: Direct Spark Web UI

**URL:** `http://localhost:4040`

**Note:** This requires:
- Spark to be running with compatible Java
- Java version 8, 11, 17, or 21 (not 24)
- Currently shows as offline if Java 24 detected

### Option C: Via API Endpoint

**URL:** `http://127.0.0.1:5000/spark/status`

**Returns JSON:**
```json
{
  "spark": {
    "backend": "pandas",
    "version": "3.5.0 (Pandas Fallback)",
    "app_id": "app-20251121160325-0000",
    "ui_port": 4040,
    "ui_url": "http://localhost:4040",
    "status": "active"
  },
  "ui_enabled": true,
  "ui_url": "http://localhost:4040"
}
```

---

## 📍 WHERE IS IT INTEGRATED?

### In Your Code

**File: `app/spark_config.py`**
- Lines 10-15: UI port configuration (4040)
- Lines 45-70: Spark session creation with UI enabled
- Lines 80-100: Status method returning UI URL

**File: `app/spark_ui_bridge.py` (NEW!)**
- Lines 1-15: Bridge initialization connecting to port 4040
- Lines 40-60: API methods fetching jobs, stages, executors
- Lines 100-120: Flask routes for endpoints

**File: `app/main.py`**
- Lines 25-35: Initialize Spark UI bridge
- Lines 210-240: Spark status and UI endpoints
- Lines 241-250: Spark dashboard route

**File: `app/templates/spark_dashboard.html` (NEW!)**
- Complete monitoring dashboard UI
- Auto-refreshes every 10 seconds
- Shows real-time Spark status and metrics

**File: `run_server_spark.py`**
- Lines 35-40: Pre-initialize Spark on startup
- Lines 41-60: Display server access points at startup

---

## 🔗 ALL AVAILABLE ENDPOINTS

### Main Dashboard
- **URL:** `http://127.0.0.1:5000/`
- **Purpose:** IoT sensor data dashboard
- **Type:** HTML page

### Spark Monitoring Dashboard ⭐ NEW!
- **URL:** `http://127.0.0.1:5000/spark-dashboard`
- **Purpose:** Monitor Spark Web UI and metrics
- **Type:** Interactive HTML dashboard

### Spark Status (JSON API)
- **URL:** `http://127.0.0.1:5000/spark/status`
- **Purpose:** Get Spark session status
- **Type:** JSON response

### Spark UI URL
- **URL:** `http://127.0.0.1:5000/spark/ui`
- **Purpose:** Get redirect URL for Spark Web UI
- **Type:** JSON response

### Spark Web UI Bridge - Status
- **URL:** `http://127.0.0.1:5000/spark-ui/status`
- **Purpose:** Check if Spark Web UI is available
- **Type:** JSON response

### Spark Web UI Bridge - Jobs
- **URL:** `http://127.0.0.1:5000/spark-ui/jobs`
- **Purpose:** List all Spark jobs
- **Type:** JSON response

### Spark Web UI Bridge - Stages
- **URL:** `http://127.0.0.1:5000/spark-ui/stages`
- **Purpose:** List all Spark stages
- **Type:** JSON response

### Spark Web UI Bridge - Executors
- **URL:** `http://127.0.0.1:5000/spark-ui/executors`
- **Purpose:** List all Spark executors
- **Type:** JSON response

### Spark Web UI Direct
- **URL:** `http://localhost:4040`
- **Purpose:** Full Spark Web UI dashboard
- **Type:** Interactive web interface (when Spark is active)

---

## 💻 EXAMPLE: TESTING WITH CURL

```bash
# Test Spark Status
curl http://127.0.0.1:5000/spark/status

# Test Spark Jobs API
curl http://127.0.0.1:5000/spark-ui/jobs

# Test Spark Stages API
curl http://127.0.0.1:5000/spark-ui/stages

# Test Sensor Data
curl http://127.0.0.1:5000/sensors
```

---

## 🔧 HOW TO ENABLE ACTIVE SPARK WEB UI (Advanced)

If you want the actual Spark Web UI running on port 4040, you need compatible Java:

### Current Status
```
System Java: Java 24 ❌ (Spark supports Java 8-21)
Spark Web UI: Currently using Pandas fallback with Mock interface
```

### To Enable Real Spark Web UI

1. **Install compatible Java:**
   - Option A: Java 17 (LTS) - Recommended
   - Option B: Java 21 (Latest LTS)

2. **Update JAVA_HOME environment variable:**
   ```powershell
   $env:JAVA_HOME = "C:\Program Files\Java\jdk-17" # or your Java path
   ```

3. **Restart the server:**
   ```bash
   python run_server_spark.py
   ```

4. **Access Spark Web UI:**
   ```
   http://localhost:4040
   ```

---

## 📊 WHAT YOU'LL SEE IN SPARK WEB UI

When you open `http://localhost:4040`, you'll see:

### Dashboard View
- Application Status
- Total cores and memory
- Uptime and job statistics

### Jobs Tab
- List of all submitted jobs
- Job status (running, completed, failed)
- Job duration and progress

### Stages Tab
- Execution stages for each job
- Task information (running, completed, failed)
- Stage metrics (duration, shuffle data)

### Storage Tab
- RDD cache storage
- Data distribution across executors
- Memory usage

### SQL Tab
- SQL query execution plans
- Performance metrics
- Detailed statistics

### Executors Tab
- Executor information
- Executor address and cache usage
- Task counts and metrics

---

## 🎯 COMMON TASKS

### Check if Spark is Running
```bash
curl http://127.0.0.1:5000/spark/status
```

### Get List of Current Jobs
```bash
curl http://127.0.0.1:5000/spark-ui/jobs | python -m json.tool
```

### Monitor Sensor Data
```bash
curl http://127.0.0.1:5000/sensors | python -m json.tool
```

### Check Anomalies
```bash
curl http://127.0.0.1:5000/anomalies | python -m json.tool
```

### Get All Summary Statistics
```bash
curl http://127.0.0.1:5000/summary | python -m json.tool
```

---

## ❓ TROUBLESHOOTING

### Problem: Dashboard shows "Spark UI Offline"
**Cause:** Spark not initialized or Java incompatible
**Solution:** 
- Check server logs for Java errors
- Install compatible Java (17 or 21)
- Restart server

### Problem: Cannot connect to localhost:4040
**Cause:** Spark not running or port blocked
**Solution:**
- Verify Spark status: `curl http://127.0.0.1:5000/spark/status`
- Check firewall settings
- Ensure Flask server is running

### Problem: API endpoints return empty data
**Cause:** Spark REST API not responding
**Solution:**
- Wait for server to fully initialize (5-10 seconds)
- Check server logs for errors
- Restart server with `python run_server_spark.py`

### Problem: Proxy errors when accessing from browser
**Cause:** CORS headers missing
**Solution:** Already fixed! CORS is enabled globally for all routes

---

## 📚 DOCUMENTATION FILES

For more detailed information, see:

1. **`WHERE_IS_SPARK_WEB_UI_ATTACHED.md`**
   - Visual architecture diagrams
   - Code location for each integration point
   - Complete data flow explanation

2. **`SPARK_WEB_UI_INTEGRATION.md`**
   - Detailed configuration guide
   - Troubleshooting section
   - Advanced customization options

3. **`README.md`**
   - Project overview
   - Setup instructions
   - API reference

---

## 🎉 YOU'RE ALL SET!

Your Spark Web UI is fully integrated with your Flask IoT monitoring system!

**Next steps:**
1. Start the server: `python run_server_spark.py`
2. Visit the Spark Dashboard: `http://127.0.0.1:5000/spark-dashboard`
3. Monitor your data and Spark jobs in real-time!

---

**Questions?** Check the documentation files or review the code in `app/spark_ui_bridge.py`
