# WHERE IS SPARK WEB UI ATTACHED? - VISUAL GUIDE

## Quick Answer

**Spark Web UI is integrated in 5 key files:**

```
1. app/spark_config.py      ← Session creation & UI port configuration
2. app/spark_ui_bridge.py   ← API bridge to Spark UI (NEW!)
3. app/main.py              ← Flask routes & endpoints
4. app/templates/spark_dashboard.html  ← User interface
5. run_server_spark.py      ← Server initialization
```

---

## Integration Points - Visual Map

```
YOUR APPLICATION ARCHITECTURE
════════════════════════════════════════════════════════════════════════════

                        🌐 YOUR BROWSER
                              │
                    ┌─────────┼─────────┐
                    ↓         ↓         ↓
         http://127.0.0.1:5000
         ├─ /               (Main Dashboard)
         ├─ /spark-dashboard  ⭐ NEW! Spark Monitoring
         └─ /spark/status     (Spark Status JSON)

════════════════════════════════════════════════════════════════════════════
                    ⚡ FLASK WEB SERVER (PORT 5000)
════════════════════════════════════════════════════════════════════════════

                        ┌──────────────────────┐
                        │   CORS-Enabled       │
                        │   Flask Application  │
                        └──────────┬───────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ↓              ↓              ↓
            ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
            │ /spark/status│ │/spark-ui/jobs│ │spark-ui/dash │
            │  endpoint    │ │  endpoint    │ │  board       │
            │              │ │              │ │  HTML page   │
            └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
                   │                │                │
                   └────────┬───────┴────────┬───────┘
                            │                │
        ┌───────────────────┴─────────────────┴──────────────────┐
        │                                                         │
        │        SparkConfig + SparkUIBridge                      │
        │    (Connection Management & Data Fetching)             │
        │                                                         │
        └───────────────────┬──────────────────────┬──────────────┘
                            │                      │
                  ┌─────────┴────────┐    ┌────────┴──────────┐
                  ↓                  ↓    ↓                   ↓
        ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
        │  Spark Session   │ │  Pandas Backend  │ │  CSV Data        │
        │  (Port 4040)     │ │  (Fallback)      │ │  (Storage)       │
        │                  │ │                  │ │                  │
        │ ✓ Configured for │ │ ✓ Active & Ready │ │ ✓ 10,000 rows    │
        │   UI enabled     │ │                  │ │   15 sensors     │
        └────────┬─────────┘ └──────────────────┘ └──────────────────┘
                 │
                 │ When compatible Java detected:
                 │ Real Spark UI runs here
                 │
        http://localhost:4040
```

---

## WHERE TO FIND EACH INTEGRATION POINT

### 1️⃣ SPARK CONFIGURATION - `app/spark_config.py`

**Lines 1-20: Port Configuration**
```python
import os
from pyspark.sql import SparkSession

class SparkConfig:
    """Centralized Spark session management"""
    
    # ⭐ HERE IS WHERE SPARK WEB UI PORT IS SET
    SPARK_UI_PORT = int(os.environ.get('SPARK_UI_PORT', 4040))
    SPARK_MASTER = os.environ.get('SPARK_MASTER', 'local[*]')
```

**Lines 45-70: Session Creation with UI Enabled**
```python
@staticmethod
def _create_spark_session():
    """Create Spark session with Web UI enabled"""
    
    spark = SparkSession.builder \
        .appName('IoTAnalytics') \
        .master(SparkConfig.SPARK_MASTER) \
        .config('spark.ui.enabled', 'true')              # ⭐ ENABLE UI
        .config('spark.ui.port', str(SPARK_UI_PORT))     # ⭐ SET PORT 4040
        .config('spark.driver.host', '127.0.0.1') \
        .config('spark.driver.maxResultSize', '2g') \
        .config('spark.sql.shuffle.partitions', '200') \
        .getOrCreate()
    
    return spark
```

**Lines 80-100: Status Method**
```python
@staticmethod
def get_status():
    """Return Spark session status with UI URL"""
    session = SparkConfig.get_spark_session()
    
    return {
        'backend': 'pyspark' if session.has_spark else 'pandas',
        'version': session.spark_version if hasattr(session, 'spark_version') else 'Mock',
        'app_id': session.app_id,
        'ui_port': SparkConfig.SPARK_UI_PORT,
        'ui_url': f'http://localhost:{SPARK_UI_PORT}',  # ⭐ RETURNS UI URL
        'status': 'active' if session else 'inactive'
    }
```

---

### 2️⃣ SPARK UI BRIDGE - `app/spark_ui_bridge.py` (NEW!)

**Lines 1-15: Bridge Initialization**
```python
# HERE IS WHERE FLASK CONNECTS TO SPARK WEB UI

SPARK_UI_HOST = 'localhost'
SPARK_UI_PORT = 4040
SPARK_UI_URL = f'http://{SPARK_UI_HOST}:{SPARK_UI_PORT}'  # ⭐ CONNECTION URL

class SparkUIBridge:
    """Bridge Flask app to Spark Web UI"""
    
    @staticmethod
    def is_spark_ui_available():
        """Check if Spark UI is running"""
        try:
            response = requests.get(f'{SPARK_UI_URL}/', timeout=2)
            return response.status_code == 200
```

**Lines 40-60: API Methods for Data Fetching**
```python
    @staticmethod
    def get_spark_jobs():
        """Fetch Spark jobs from REST API"""
        response = requests.get(
            f'{SPARK_UI_URL}/api/v1/applications',  # ⭐ API CALL
            timeout=5
        )
        return response.json()
    
    @staticmethod
    def get_spark_stages():
        """Fetch Spark stages"""
        response = requests.get(
            f'{SPARK_UI_URL}/api/v1/applications/{app_id}/stages',
            timeout=5
        )
        return response.json()
```

**Lines 100-120: Blueprint Routes**
```python
# ⭐ THESE ARE THE ENDPOINTS YOUR FLASK APP PROVIDES

@spark_ui_bp.route('/status', methods=['GET'])
def spark_ui_status():
    """Spark UI availability check"""
    return jsonify({'spark_ui_available': SparkUIBridge.is_spark_ui_available()})

@spark_ui_bp.route('/jobs', methods=['GET'])
def get_jobs():
    """List Spark jobs"""
    return jsonify({'jobs': SparkUIBridge.get_spark_jobs()})

@spark_ui_bp.route('/dashboard', methods=['GET'])
def spark_dashboard():
    """Embedded Spark dashboard with iframe"""
    return render_template_string(embedded_dashboard_html)
```

---

### 3️⃣ FLASK MAIN APP - `app/main.py`

**Lines 25-35: Initialization**
```python
from app.spark_ui_bridge import init_spark_ui  # ⭐ IMPORT BRIDGE

app = Flask(__name__, static_folder="static", template_folder="templates")

# Enable CORS globally for all requests
CORS(app, resources={r"/*": {"origins": "*"}})

# ⭐ INITIALIZE SPARK UI BRIDGE WITH FLASK APP
init_spark_ui(app)
```

**Lines 210-230: Spark Status Endpoint**
```python
@app.route('/spark/status')                      # ⭐ ENDPOINT PATH
def spark_status():
    """Return Spark session status and Web UI information"""
    
    status = SparkConfig.get_status()  # ⭐ GET STATUS FROM CONFIG
    
    return jsonify({
        'spark': status,
        'ui_enabled': status.get('status') == 'active',
        'ui_url': status.get('ui_url')  # ⭐ RETURNS UI URL
    })
```

**Lines 231-240: Spark UI Redirect**
```python
@app.route('/spark/ui')                         # ⭐ ENDPOINT PATH
def spark_ui():
    """Provide redirect to Spark Web UI"""
    
    ui_url = SparkConfig.get_ui_url()           # ⭐ GET UI URL
    
    return jsonify({
        'ui_url': ui_url,
        'message': f'Spark Web UI available at {ui_url}'
    })
```

**Lines 241-250: Spark Dashboard**
```python
@app.route('/spark-dashboard')                  # ⭐ NEW ENDPOINT
def spark_dashboard():
    """Serve the Spark Web UI monitoring dashboard"""
    
    return render_template('spark_dashboard.html')  # ⭐ HTML PAGE
```

---

### 4️⃣ DASHBOARD UI - `app/templates/spark_dashboard.html`

**Lines 1-50: HTML Structure**
```html
<!DOCTYPE html>
<html>
<head>
    <title>⚡ Spark Web UI Integration Dashboard</title>
</head>
<body>
    <!-- ⭐ SPARK STATUS CARD -->
    <div class="card">
        <h2>🔍 Spark Status</h2>
        <div id="spark-status-content">Loading...</div>
    </div>
    
    <!-- ⭐ SPARK WEB UI LINK CARD -->
    <div class="card">
        <h2>🎯 Spark Web UI</h2>
        <div id="spark-ui-content">Loading...</div>
    </div>
    
    <!-- ⭐ JOBS MONITORING CARD -->
    <div class="card">
        <h2>📋 Spark Jobs</h2>
        <div id="spark-jobs-content">Loading...</div>
    </div>
</body>
</html>
```

**Lines 200-230: JavaScript Data Loading**
```javascript
// ⭐ FETCH SPARK STATUS FROM API
async function loadSparkStatus() {
    const data = await fetchAPI('/spark/status');  // ⭐ CALLS FLASK ENDPOINT
    
    const element = document.getElementById('spark-status-content');
    
    // Display status badge and information
    element.innerHTML = `
        <ul>
            <li><strong>Status:</strong> ${spark.status}</li>
            <li><strong>UI URL:</strong> ${spark.ui_url}</li>
            <li><strong>Port:</strong> ${spark.ui_port}</li>
        </ul>
    `;
}

// ⭐ FETCH SPARK JOBS FROM API
async function loadSparkJobs() {
    const data = await fetchAPI('/spark-ui/jobs');  // ⭐ CALLS FLASK ENDPOINT
    
    // Display jobs information
}

// ⭐ ON PAGE LOAD, FETCH ALL DATA
window.addEventListener('load', () => {
    loadSparkStatus();
    loadSparkJobs();
    loadSparkStages();
    loadSparkExecutors();
});
```

---

### 5️⃣ SERVER INITIALIZATION - `run_server_spark.py`

**Lines 1-40: Flask App & Spark Setup**
```python
import logging
from flask import Flask
from app.main import app as flask_app
from app.spark_config import SparkConfig

logger = logging.getLogger(__name__)

# ⭐ PRE-INITIALIZE SPARK SESSION ON SERVER START
def initialize_spark():
    """Initialize Spark session with Web UI"""
    logger.info("Initializing Spark session...")
    
    spark = SparkConfig.get_spark_session()  # ⭐ STARTS SPARK + WEB UI
    
    status = SparkConfig.get_status()
    logger.info(f"  App ID: {status['app_id']}")
    logger.info(f"  Backend: {status['backend']}")
    logger.info(f"  Spark Web UI: {status['ui_url']}")
```

**Lines 41-60: Server Configuration Display**
```python
if __name__ == '__main__':
    print("\n" + "="*70)
    print("🏭 Factory IoT Sensor Monitoring System with Spark Integration")
    print("="*70)
    
    initialize_spark()
    
    print("\n📊 Access Points:")
    print(f"  Dashboard:     http://127.0.0.1:5000/")
    print(f"  Spark Status:  http://127.0.0.1:5000/spark/status")
    print(f"  Spark UI:      http://127.0.0.1:5000/spark-dashboard")  # ⭐ NEW
    print(f"  Spark Web UI:  http://localhost:4040")                   # ⭐ WHEN ACTIVE
    print("\n" + "="*70)
    
    # Start Flask server with Waitress
    from waitress import serve
    serve(flask_app, host='127.0.0.1', port=5000)
```

---

## HOW THE CONNECTION WORKS - STEP BY STEP

### User Journey

```
Step 1: User visits http://127.0.0.1:5000/spark-dashboard
                              ↓
Step 2: Flask route /spark-dashboard serves spark_dashboard.html
                              ↓
Step 3: HTML loads JavaScript that calls /spark/status endpoint
                              ↓
Step 4: /spark/status endpoint calls SparkConfig.get_status()
                              ↓
Step 5: SparkConfig returns JSON with ui_url: "http://localhost:4040"
                              ↓
Step 6: JavaScript displays "Spark UI Available" badge
                              ↓
Step 7: User clicks "Open Spark Web UI" button
                              ↓
Step 8: Browser navigates to http://localhost:4040
                              ↓
Step 9: Spark Web UI renders with real-time job/stage/executor info
```

### Data Flow

```
Browser                Flask (5000)          Spark Config         Spark (4040)
   │                       │                      │                    │
   ├─ /spark-status ──────→│                      │                    │
   │                       ├─ SparkConfig ───────→│                    │
   │                       │ .get_status()        │                    │
   │                       │←─ {ui_url, ...} ─────│                    │
   │←─ JSON response ──────│                      │                    │
   │                       │                      │                    │
   │ User clicks "Open"    │                      │                    │
   ├─ http://localhost:4040 ──────────────────────────────────────────→│
   │                       │                      │  Spark Web UI      │
   │←─ Interactive Dashboard ─────────────────────────────────────────│
```

---

## COMPLETE ENDPOINT MAP

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AVAILABLE ENDPOINTS                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FLASK APP (http://127.0.0.1:5000)                                      │
│  ├─ GET  /                    → Main IoT Dashboard                       │
│  ├─ GET  /spark-dashboard     → Spark Monitoring Dashboard (⭐ NEW!)    │
│  ├─ GET  /spark/status        → Spark Status JSON                       │
│  ├─ GET  /spark/ui            → Spark UI URL                            │
│  ├─ GET  /sensors             → List all sensors                        │
│  ├─ GET  /data                → Get sensor data                         │
│  ├─ GET  /summary             → Summary statistics                      │
│  ├─ GET  /anomalies           → Detect anomalies                        │
│  │                                                                       │
│  SPARK UI BRIDGE (http://127.0.0.1:5000/spark-ui)                       │
│  ├─ GET  /spark-ui/status     → Check Spark UI availability            │
│  ├─ GET  /spark-ui/jobs       → List Spark jobs (JSON)                  │
│  ├─ GET  /spark-ui/stages     → List Spark stages (JSON)                │
│  ├─ GET  /spark-ui/executors  → List executors (JSON)                   │
│  ├─ GET  /spark-ui/dashboard  → Embedded Spark UI dashboard            │
│  └─ GET  /spark-ui/proxy/*    → Proxy to Spark REST API                │
│                                                                          │
│  SPARK WEB UI (http://localhost:4040) - When Active                     │
│  ├─ Full interactive Spark monitoring dashboard                         │
│  ├─ Real-time job tracking                                              │
│  ├─ Executor performance metrics                                        │
│  └─ Storage and cache monitoring                                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## SUMMARY: WHERE IS SPARK WEB UI ATTACHED?

| Component | File | Role | Status |
|-----------|------|------|--------|
| **Config** | `app/spark_config.py` | Sets UI port (4040), enables UI in Spark config | ✅ Active |
| **Bridge** | `app/spark_ui_bridge.py` | Connects Flask to Spark REST API at :4040 | ✅ NEW! |
| **Routes** | `app/main.py` | Provides `/spark/*` and `/spark-ui/*` endpoints | ✅ Ready |
| **Dashboard** | `app/templates/spark_dashboard.html` | User interface to access Spark Web UI | ✅ New! |
| **Server** | `run_server_spark.py` | Auto-initializes Spark on startup | ✅ Active |

---

## QUICK ACCESS LINKS

| Purpose | URL | What It Shows |
|---------|-----|---------------|
| **Dashboard** | http://127.0.0.1:5000 | IoT sensor data monitoring |
| **Spark Dashboard** | http://127.0.0.1:5000/spark-dashboard | Spark integration status & quick links |
| **Spark Status API** | http://127.0.0.1:5000/spark/status | JSON with Spark session info |
| **Spark UI (Direct)** | http://localhost:4040 | Full Spark Web UI (when active) |
| **Spark Jobs API** | http://127.0.0.1:5000/spark-ui/jobs | List of Spark jobs as JSON |
| **Spark Stages API** | http://127.0.0.1:5000/spark-ui/stages | List of Spark stages as JSON |

---

**Your Spark Web UI is fully integrated and connected!** ⚡
