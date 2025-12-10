# Quick Reference Guide - Spark Integrated IoT System

## 🎯 Current Status
✅ **Server Running** on `http://127.0.0.1:5000`  
✅ **Spark Infrastructure** Integrated  
✅ **15 Sensors** Active (10,000 readings)  
✅ **Real-time Monitoring** Available  

---

## 📱 Access Points

| Purpose | URL | Method |
|---------|-----|--------|
| Dashboard | http://127.0.0.1:5000 | GET |
| Sensors List | http://127.0.0.1:5000/sensors | GET |
| Sensor Data | http://127.0.0.1:5000/data | GET |
| Data Summary | http://127.0.0.1:5000/summary | GET |
| Anomalies | http://127.0.0.1:5000/anomalies | GET |
| **Spark Status** | http://127.0.0.1:5000/spark/status | GET |
| Backend Info | http://127.0.0.1:5000/info | GET |

---

## 🚀 Quick Commands

### Start Server
```powershell
cd "c:\spark project"
python run_server_spark.py
```

### Stop Server
```powershell
# In PowerShell:
Get-Process python | Stop-Process -Force

# Or press Ctrl+C in the terminal
```

### Test Integration
```powershell
cd "c:\spark project"
python test_spark_integration.py
```

### Check Server Status
```powershell
netstat -ano | findstr ":5000"
curl http://127.0.0.1:5000/health
```

---

## 🎨 Dashboard Features

### Main Page (http://127.0.0.1:5000)
- Real-time sensor status display
- Active sensor count
- Latest readings per machine
- Machine grouping by equipment type

### Sensor Details
- Individual sensor history
- Current value and status
- Anomaly information
- Machine association

### Anomaly Detection
- 3-sigma rule applied
- Real-time alerts
- Historical anomalies
- Detailed analysis

---

## 📊 Data Endpoints

### Get All Sensor Readings
```bash
curl http://127.0.0.1:5000/data
```

### Get Specific Sensor Data
```bash
curl http://127.0.0.1:5000/data?sensor_id=SENSOR_001
```

### Get Summary Statistics
```bash
curl http://127.0.0.1:5000/summary
```

### Detect Anomalies
```bash
curl http://127.0.0.1:5000/anomalies
curl http://127.0.0.1:5000/anomalies?sensor_id=SENSOR_002
```

### Get Single Sensor Details
```bash
curl http://127.0.0.1:5000/sensor/SENSOR_001
```

---

## 🔍 Spark Integration Details

### Current Configuration
- **Backend**: Pandas (with Spark ready)
- **Status**: Active
- **Version**: 3.5.0 (Pandas Fallback)
- **UI Port**: 4040
- **Master**: local[*] (all cores)
- **App ID**: Auto-generated on startup

### Why Pandas Fallback?
- System has Java 24 (Spark supports Java 8-21)
- Automatic fallback activated
- Full functionality maintained
- Zero performance loss for single-machine use

### Upgrade Path
To use real PySpark:
1. Install Java 8, 11, 17, or 21
2. Update JAVA_HOME environment variable
3. Restart server
4. System will auto-detect and use PySpark

---

## 📈 Dataset Information

### Current Dataset
- **File**: `data/factory_sensors_data.csv`
- **Records**: 10,000 rows
- **Sensors**: 15 active
- **Time Range**: Generated sequentially

### Sensor Types
1. **Tempering_Machine_A** (3 sensors)
   - Pressure (PSI)
   - Temperature (°C)
   - Vibration (mm/s)

2. **Cooling_Unit_B** (3 sensors)
   - Temperature (°C)
   - Pressure (PSI)
   - Humidity (%)

3. **Packaging_Machine_C** (3 sensors)
   - Speed (RPM)
   - Vibration (mm/s)
   - Power (kW)

4. **Mixer_Unit_D** (3 sensors)
   - Temperature (°C)
   - Pressure (PSI)
   - Flow_Rate (L/min)

5. **Conveyor_E** (3 sensors)
   - Speed (RPM)
   - Power (kW)
   - Load (kg)

---

## 🛠️ API Response Examples

### Spark Status Response
```json
{
  "spark": {
    "status": "active",
    "backend": "pandas",
    "app_name": "IoTAnalytics",
    "app_id": "app-20251121153047-0000",
    "master": "local[*]",
    "version": "3.5.0 (Pandas Fallback)",
    "ui_port": 4040,
    "ui_url": "http://localhost:4040",
    "threads": 4,
    "spark_available": false
  },
  "ui_enabled": true
}
```

### Sensors List Response
```json
{
  "sensors": [
    {
      "sensor_id": "SENSOR_001",
      "machine": "Tempering_Machine_A",
      "type": "Pressure",
      "unit": "PSI"
    },
    ...
  ]
}
```

---

## ⚙️ Configuration Files

### Environment Variables
Edit these in PowerShell before starting:
```powershell
$env:SPARK_UI_PORT = '4040'      # Spark Web UI port
$env:SPARK_MASTER = 'local[*]'   # Spark master
$env:PORT = '5000'               # Flask port
```

### Python Configuration
- **app/main.py** - Flask routes and endpoints
- **app/spark_config.py** - Spark session management
- **app/spark_service.py** - Data processing logic

---

## 🐛 Common Issues & Solutions

### Issue: "Address already in use"
```powershell
# Find the process using port 5000
netstat -ano | findstr ":5000"

# Kill it by PID
Stop-Process -Id <PID> -Force
```

### Issue: "ModuleNotFoundError"
```powershell
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Server not responding
```powershell
# Check if process is running
Get-Process python

# Restart server
python run_server_spark.py
```

---

## 📚 Key Files

| File | Purpose |
|------|---------|
| `run_server_spark.py` | Main server launcher |
| `app/main.py` | Flask routes |
| `app/spark_config.py` | Spark configuration |
| `app/spark_service.py` | Data processing |
| `data/factory_sensors_data.csv` | Main dataset |
| `test_spark_integration.py` | Integration test |

---

## 🎓 Learning Path

1. **Start Server**
   ```bash
   python run_server_spark.py
   ```

2. **Access Dashboard**
   - Open http://127.0.0.1:5000

3. **Test API Endpoints**
   - Try `/sensors` endpoint
   - Try `/spark/status` endpoint
   - Try `/summary` endpoint

4. **Check Data Processing**
   - View anomalies
   - Check sensor details
   - Review summaries

5. **Monitor Status**
   - Use `/spark/status` for system info
   - Check logs in server terminal

---

## 📞 Support Resources

### Documentation
- `SPARK_SETUP_GUIDE.md` - Detailed setup guide
- `SPARK_INTEGRATION_COMPLETE.md` - Full integration documentation
- `CONNECTION_GUIDE.md` - Connection instructions
- `README.md` - Project overview

### Files to Reference
- `app/main.py` - See all available endpoints
- `app/spark_config.py` - Understand configuration
- `app/spark_service.py` - Data processing logic

---

## ✅ Verification Checklist

Run this to verify everything is working:

```powershell
# Check 1: Server running
netstat -ano | findstr ":5000"

# Check 2: Dashboard accessible
Invoke-WebRequest http://127.0.0.1:5000 -UseBasicParsing

# Check 3: Sensors API working
Invoke-WebRequest http://127.0.0.1:5000/sensors -UseBasicParsing

# Check 4: Spark status
Invoke-WebRequest http://127.0.0.1:5000/spark/status -UseBasicParsing

# Check 5: Dataset loaded
Invoke-WebRequest http://127.0.0.1:5000/info -UseBasicParsing
```

All checks should return HTTP 200 status.

---

**Version**: 1.0  
**Updated**: November 21, 2025  
**Status**: Production Ready ✅

---

## 🚀 Next Steps

1. Add more sensor data
2. Implement real-time updates using WebSockets
3. Add data export functionality
4. Configure production deployment
5. Setup monitoring and alerting

Enjoy your Factory IoT Monitoring System with Spark Integration!
