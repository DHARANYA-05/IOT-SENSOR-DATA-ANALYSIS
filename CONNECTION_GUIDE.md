# Factory IoT Sensor Monitoring System - Connection Guide

## 🏭 System is Running!

### Server Status
- ✅ **Status**: Running on port 5000
- ✅ **Your Device IP**: 172.2.5.43
- ✅ **Network Access**: Enabled (all devices on network can access)

---

## 📱 How to Access from Other Devices

### Option 1: From Another Device on Same Network
Open browser and go to:
```
http://172.2.5.43:5000
```

### Option 2: From This Device (Localhost)
```
http://127.0.0.1:5000
http://localhost:5000
```

---

## 🌐 Available Endpoints

All endpoints are accessible from any device on your network:

### Dashboard & Static Files
- **Dashboard UI**: `GET http://172.2.5.43:5000/`
- **Styles**: `GET http://172.2.5.43:5000/static/styles.css`
- **JavaScript**: `GET http://172.2.5.43:5000/static/app.js`

### API Endpoints (JSON)

#### List All Sensors
```
GET http://172.2.5.43:5000/sensors
```
Returns list of all 15 sensors with metadata

#### Get Specific Sensor Details
```
GET http://172.2.5.43:5000/sensor/<SENSOR_ID>
Example: http://172.2.5.43:5000/sensor/SENSOR_001
```
Returns: sensor metadata + anomalies for that sensor

#### Get Sensor Data
```
GET http://172.2.5.43:5000/data?sensor_id=<SENSOR_ID>
Example: http://172.2.5.43:5000/data?sensor_id=SENSOR_001
```
Returns: time-series data points for selected sensor

#### Get All Anomalies
```
GET http://172.2.5.43:5000/anomalies
```
Returns: all detected anomalies across all sensors

#### Get Anomalies for Specific Sensor
```
GET http://172.2.5.43:5000/anomalies?sensor_id=<SENSOR_ID>
Example: http://172.2.5.43:5000/anomalies?sensor_id=SENSOR_001
```

#### Server Info
```
GET http://172.2.5.43:5000/info
```
Returns: backend type, dataset info, row count

#### Health Check
```
GET http://172.2.5.43:5000/health
```
Returns: `{"status": "ok"}`

---

## 🔌 Connection from External Devices

If you want to connect from:
- **Mobile Device**: Use `http://172.2.5.43:5000`
- **Tablet**: Use `http://172.2.5.43:5000`
- **Laptop on WiFi**: Use `http://172.2.5.43:5000`
- **Remote Server**: Use `http://172.2.5.43:5000`

---

## 📊 Data Structure

### Sensor List Response
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

### Sensor Details Response
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
    },
    ...
  ]
}
```

### Sensor Data Response
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

---

## 🎯 15 Sensors Monitored

### Tempering Machine A
- SENSOR_001: Pressure (PSI)
- SENSOR_002: Temperature (°C)
- SENSOR_003: Vibration (mm/s)

### Cooling Unit B
- SENSOR_004: Temperature (°C)
- SENSOR_005: Pressure (PSI)
- SENSOR_006: Humidity (%)

### Packaging Machine C
- SENSOR_007: Speed (RPM)
- SENSOR_008: Vibration (mm/s)
- SENSOR_009: Power (kW)

### Mixer Unit D
- SENSOR_010: Temperature (°C)
- SENSOR_011: Pressure (PSI)
- SENSOR_012: Flow Rate (L/min)

### Conveyor E
- SENSOR_013: Speed (RPM)
- SENSOR_014: Power (kW)
- SENSOR_015: Load (kg)

---

## 🔧 Server Details

- **Backend**: Flask 2.3.2
- **Server**: Gevent WSGI
- **Port**: 5000
- **Data**: CSV with 10,000 sensor readings
- **Analysis**: Pandas (PySpark optional)
- **Anomaly Detection**: 3-sigma method per sensor

---

## 🚀 Quick Start from Another Device

1. Make sure this device (172.2.5.43) has the server running
2. On any other device, open browser
3. Go to: `http://172.2.5.43:5000`
4. Dashboard loads with all 15 sensors
5. Click any sensor to view details, chart, and anomalies

---

## ⚠️ Firewall Notes

If you can't connect from another device:
1. Check if Windows Firewall is blocking port 5000
2. Add exception for Python.exe on port 5000
3. Or temporarily disable firewall for testing

---

## 📋 Features

✅ Real-time sensor monitoring dashboard
✅ 15 sensors across 5 factory machines
✅ Time-series visualization with Chart.js
✅ Anomaly detection (3-sigma rule)
✅ RESTful API endpoints
✅ Responsive UI (Bootstrap 5)
✅ Network accessible
✅ JSON data export ready

---

**Server Running**: ✅ 172.2.5.43:5000
**Status**: Ready for connections
