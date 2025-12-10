# 🏭 Factory IoT Sensor Monitoring System - Setup Complete

## ✅ System Status: RUNNING

### Server Information
```
Device IP: 172.2.5.43
Port: 5000
Protocol: HTTP
Status: Active and Listening
```

---

## 🌐 How to Connect Your Web UI

### From Your Device (This Computer)
```
http://127.0.0.1:5000
http://localhost:5000
```

### From Other Devices on Same Network
```
http://172.2.5.43:5000
```

---

## 📱 Testing the Connection

### Test 1: Check if Server is Running
```bash
curl http://172.2.5.43:5000/health
```
Expected Response: `{"status": "ok"}`

### Test 2: Get List of All Sensors
```bash
curl http://172.2.5.43:5000/sensors
```

### Test 3: Get Data for Specific Sensor
```bash
curl http://172.2.5.43:5000/sensor/SENSOR_001
curl http://172.2.5.43:5000/data?sensor_id=SENSOR_001
```

---

## 🔗 API Integration Guide

### RESTful Endpoints Available

#### 1. Get All Sensors
**URL**: `GET /sensors`
**Response**: List of 15 sensors with metadata
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

#### 2. Get Sensor Details & Anomalies
**URL**: `GET /sensor/<SENSOR_ID>`
**Example**: `GET /sensor/SENSOR_001`
```json
{
  "metadata": {
    "sensor_id": "SENSOR_001",
    "machine": "Tempering_Machine_A",
    "type": "Pressure",
    "unit": "PSI"
  },
  "anomalies": [
    {
      "sensor_id": "SENSOR_001",
      "machine": "Tempering_Machine_A",
      "timestamp": "2025-01-01T01:37:54",
      "type": "Pressure",
      "value": 51.12,
      "unit": "PSI",
      "reason": "value outside 3*stddev"
    }
  ]
}
```

#### 3. Get Time-Series Data
**URL**: `GET /data?sensor_id=<SENSOR_ID>`
**Example**: `GET /data?sensor_id=SENSOR_001`
```json
{
  "data": [
    {
      "sensor_id": "SENSOR_001",
      "machine": "Tempering_Machine_A",
      "timestamp": "2025-01-01T00:00:26",
      "type": "Pressure",
      "value": 32.8,
      "unit": "PSI",
      "status": "normal"
    },
    ...
  ]
}
```

#### 4. Get All Anomalies
**URL**: `GET /anomalies`
**Filtered**: `GET /anomalies?sensor_id=<SENSOR_ID>`

#### 5. Server Info
**URL**: `GET /info`
**Response**: Backend type, dataset info, row count

#### 6. Health Check
**URL**: `GET /health`
**Response**: `{"status": "ok"}`

---

## 📊 Available Sensors (15 Total)

### Tempering Machine A
- **SENSOR_001**: Pressure (PSI)
- **SENSOR_002**: Temperature (°C)
- **SENSOR_003**: Vibration (mm/s)

### Cooling Unit B
- **SENSOR_004**: Temperature (°C)
- **SENSOR_005**: Pressure (PSI)
- **SENSOR_006**: Humidity (%)

### Packaging Machine C
- **SENSOR_007**: Speed (RPM)
- **SENSOR_008**: Vibration (mm/s)
- **SENSOR_009**: Power (kW)

### Mixer Unit D
- **SENSOR_010**: Temperature (°C)
- **SENSOR_011**: Pressure (PSI)
- **SENSOR_012**: Flow Rate (L/min)

### Conveyor E
- **SENSOR_013**: Speed (RPM)
- **SENSOR_014**: Power (kW)
- **SENSOR_015**: Load (kg)

---

## 🔧 Integrating with Your Web UI

### JavaScript/Frontend Integration Example

```javascript
// Fetch all sensors
fetch('http://172.2.5.43:5000/sensors')
  .then(response => response.json())
  .then(data => {
    console.log('Sensors:', data.sensors);
    // Display sensors in your UI
  });

// Fetch specific sensor data
fetch('http://172.2.5.43:5000/sensor/SENSOR_001')
  .then(response => response.json())
  .then(data => {
    console.log('Sensor Details:', data.metadata);
    console.log('Anomalies:', data.anomalies);
  });

// Fetch time-series data
fetch('http://172.2.5.43:5000/data?sensor_id=SENSOR_001')
  .then(response => response.json())
  .then(data => {
    console.log('Data Points:', data.data);
    // Plot chart with data
  });
```

### Python/Backend Integration Example

```python
import requests

# Get all sensors
response = requests.get('http://172.2.5.43:5000/sensors')
sensors = response.json()['sensors']

# Get specific sensor data
response = requests.get('http://172.2.5.43:5000/data?sensor_id=SENSOR_001')
data = response.json()['data']

# Get anomalies
response = requests.get('http://172.2.5.43:5000/anomalies')
anomalies = response.json()['alerts']
```

---

## 🔐 Security Notes

- **Current Mode**: Development (localhost + network accessible)
- **Firewall**: May need to allow Python.exe on port 5000
- **CORS**: Not currently enabled (use same origin for frontend)

### To Enable CORS (if needed):
Add to `app/main.py`:
```python
from flask_cors import CORS
CORS(app)
```

Install: `pip install flask-cors`

---

## 📈 Data Features

- **Total Readings**: 10,000 sensor data points
- **Time Period**: Jan 1 - Jan 2, 2025
- **Anomaly Detection**: 3-sigma statistical method per sensor
- **Data Format**: JSON/REST API
- **Response Time**: <500ms per request

---

## 🚀 Dashboard Features

✅ Real-time sensor monitoring
✅ Interactive charts (Chart.js)
✅ Anomaly alerts & notifications
✅ Time-series visualization
✅ Responsive design (Mobile + Desktop)
✅ Sensor filtering & search
✅ Machine-specific views
✅ Global anomaly overview

---

## 📝 File Structure

```
c:\spark project\
├── server.py              # Main server (CHANGE: 0.0.0.0 binding)
├── app/
│   ├── main.py           # Flask routes & endpoints
│   ├── spark_service.py  # Data processing
│   ├── templates/
│   │   └── index.html    # Dashboard UI
│   └── static/
│       ├── app.js        # Dashboard logic
│       └── styles.css    # Dashboard styling
├── data/
│   └── factory_sensors_data.csv  # 10,000 sensor readings
└── CONNECTION_GUIDE.md   # This file
```

---

## 🔧 Troubleshooting

### Can't Connect from Another Device?
1. Check server is running: `http://172.2.5.43:5000/health`
2. Check firewall allows port 5000
3. Verify both devices on same network
4. Check IP: Run `ipconfig` on server device

### Dashboard Not Loading?
1. Clear browser cache
2. Check browser console for errors (F12)
3. Verify `/static/app.js` and `/static/styles.css` load
4. Check server logs for errors

### API Returns Errors?
1. Check sensor ID exists: `GET /sensors`
2. Verify timestamp format in requests
3. Check server logs for detailed errors

---

## 📞 Support

**Server Logs**: Check PowerShell terminal running `server.py`
**API Docs**: All endpoints documented above
**Data Schema**: JSON responses shown in integration examples

---

## ✨ Quick Start Checklist

- [x] Server installed and configured
- [x] Port 5000 accessible
- [x] All 15 sensors registered
- [x] 10,000 data points loaded
- [x] Dashboard UI ready
- [x] API endpoints available
- [x] Network access enabled
- [x] Ready for integration

---

**System Ready!** 🎉
Your Factory IoT monitoring system is running and ready to receive connections from your web UI at:
- **Local**: http://127.0.0.1:5000
- **Network**: http://172.2.5.43:5000

