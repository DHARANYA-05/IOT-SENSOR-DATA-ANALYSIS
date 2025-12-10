# IoT Project with Apache Spark Web UI Integration

## Project Overview

Your **IoT Analytics Application** is now fully integrated with **Apache Spark**. All IoT data processing operations execute as Spark jobs visible in the Spark Web UI.

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   Flask Web Application (Port 5000)             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ IoT Dashboard                                             │  │
│  │ - Real-time sensor monitoring (15 sensors, 5 machines)   │  │
│  │ - Anomaly detection (3-sigma rule)                       │  │
│  │ - Live data visualization                                │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Spark Jobs Control Center                                │  │
│  │ - Submit IoT operations as Spark jobs                    │  │
│  │ - Monitor job execution and statistics                   │  │
│  │ - Real-time job tracking                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Integrated Dashboard                                     │  │
│  │ - Combined IoT Analytics + Spark Monitoring              │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   IoT Spark Jobs Module                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ /spark/iot/analyze-sensors                               │  │
│  │ /spark/iot/detect-anomalies                              │  │
│  │ /spark/iot/sensor-summary                                │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              Apache Spark (local[*] mode)                       │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Spark RDD Operations                                     │  │
│  │ - Data Processing                                        │  │
│  │ - Statistical Analysis                                   │  │
│  │ - Aggregations                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         Spark Web UI (Port 4040 or 4041)                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Jobs - View all submitted jobs                           │  │
│  │ Stages - Monitor task execution                          │  │
│  │ Executors - View cluster resources                       │  │
│  │ Environment - Check Spark configuration                  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Available Dashboards

### 1. Main IoT Dashboard
- **URL**: http://127.0.0.1:5000/
- **Features**:
  - Real-time sensor data for 15 sensors
  - Machine status monitoring (5 machines)
  - Anomaly detection and alerts
  - Sensor data visualization
  - Historical data analysis

### 2. Spark Jobs Control Center
- **URL**: http://127.0.0.1:5000/spark-jobs
- **Features**:
  - Submit IoT operations as Spark jobs
  - 3 IoT-specific job types:
    - **Analyze Sensors**: Statistical analysis of all sensors
    - **Detect Anomalies**: Find outliers using 3-sigma rule
    - **Sensor Summary**: Group and aggregate by sensor
  - Job statistics dashboard
  - Live job monitoring with auto-refresh
  - Direct links to Spark Web UI

### 3. Integrated Dashboard
- **URL**: http://127.0.0.1:5000/integrated-dashboard
- **Features**:
  - Combined IoT + Spark monitoring
  - Job execution status display
  - Embedded Spark Web UI
  - Cluster metrics

## IoT Spark Jobs

### Job 1: Analyze Sensors
```
Endpoint: POST /spark/iot/analyze-sensors
Purpose: Analyze all sensor data using Spark RDD operations
Output: min, max, avg, sum statistics
Spark Operations: count(), map(), sum(), min(), max()
```

### Job 2: Detect Anomalies
```
Endpoint: POST /spark/iot/detect-anomalies
Purpose: Detect outliers using 3-sigma statistical rule
Output: Anomaly count, mean, stddev, bounds, percentage
Spark Operations: groupBy(), filter(), variance calculation
```

### Job 3: Sensor Summary
```
Endpoint: POST /spark/iot/sensor-summary
Purpose: Group sensor data and generate statistics per sensor
Output: Total sensors, readings, per-sensor metrics
Spark Operations: groupByKey(), map(), collect()
```

## How to Use

### Option A: Web UI (Recommended)

1. **Start the Application**:
   ```bash
   cd "c:\spark project"
   python server.py
   ```

2. **Open IoT Dashboard**:
   - Navigate to: http://127.0.0.1:5000/
   - View live sensor data and anomalies

3. **Submit Spark Jobs**:
   - Click "Spark Jobs" button in navbar
   - Or navigate to: http://127.0.0.1:5000/spark-jobs
   - Click any button in "IoT Operations" section:
     - "Analyze Sensors"
     - "Detect Anomalies"
     - "Sensor Summary"

4. **Monitor Job Execution**:
   - Click "Access Spark Web UI" button
   - Or visit: http://localhost:4040
   - Watch jobs execute in real-time

### Option B: Direct API Calls

```bash
# Analyze sensors
curl -X POST http://127.0.0.1:5000/spark/iot/analyze-sensors

# Detect anomalies
curl -X POST http://127.0.0.1:5000/spark/iot/detect-anomalies

# Sensor summary
curl -X POST http://127.0.0.1:5000/spark/iot/sensor-summary

# Get all jobs
curl http://127.0.0.1:5000/spark/jobs
```

### Option C: Python Client

```python
import requests

# Submit job
response = requests.post('http://127.0.0.1:5000/spark/iot/analyze-sensors')
print(response.json())

# Get job status
response = requests.get('http://127.0.0.1:5000/spark/jobs')
print(response.json())
```

## Key Features

✅ **Real-time IoT Monitoring**
- 15 sensors across 5 production machines
- Live data streaming and visualization
- Anomaly detection and alerts

✅ **Spark Integration**
- IoT operations execute as Spark jobs
- Full Spark Web UI visibility
- Job tracking and monitoring

✅ **Three IoT-Specific Spark Jobs**
- Sensor Analysis: Statistical calculations
- Anomaly Detection: Outlier identification
- Sensor Summary: Grouped aggregations

✅ **Multiple Dashboards**
- Main IoT Dashboard (sensor data)
- Spark Jobs Control (job submission)
- Integrated Dashboard (combined view)

✅ **31 Total Endpoints**
- IoT data endpoints
- Spark job submission endpoints
- Spark monitoring endpoints
- Status and health check endpoints

## Technical Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.10 | Application runtime |
| Flask | 2.3.2 | Web framework |
| Pandas | 2.1.3 | Data processing |
| PySpark | 3.5.0 | Distributed computing |
| Bootstrap | 5.3.0 | UI framework |
| Chart.js | Latest | Data visualization |

## Configuration

### Spark Settings
- **Master**: `local[*]` (all available cores)
- **App Name**: `IoTAnalytics`
- **UI Port**: 4040 (or 4041 if 4040 is in use)

### Flask Settings
- **Host**: 127.0.0.1
- **Port**: 5000
- **Debug**: False (production mode)

### Data Files
- **Primary**: `data/factory_sensors_data.csv`
- **Contains**: 15 sensors × 5 machines
- **Columns**: sensor_id, machine, timestamp, type, value, unit, status

## Performance Metrics

- **Routes**: 31 endpoints
- **Sensors**: 15 active sensors
- **Machines**: 5 production machines
- **Job Execution**: Real-time in Spark
- **Auto-refresh**: 3-10 second intervals

## Troubleshooting

### Spark Web UI not visible
- Check if port 4040 or 4041 is in use
- Spark automatically uses next available port
- Look for "Service 'SparkUI' bound on port XXXX" in logs

### Jobs not showing in Spark UI
- Ensure Spark initialization shows "READY"
- Check Flask server is running on 127.0.0.1:5000
- Try refreshing Spark Web UI page

### Data not loading
- Verify `data/factory_sensors_data.csv` exists
- Check file has headers: sensor_id, machine, timestamp, etc.
- Ensure CSV is properly formatted

## Next Steps

1. **Explore IoT Data**:
   - Visit http://127.0.0.1:5000/
   - Select different sensors
   - View historical trends

2. **Submit Spark Jobs**:
   - Go to http://127.0.0.1:5000/spark-jobs
   - Click IoT operation buttons
   - Monitor execution in Spark Web UI

3. **Customize Operations**:
   - Edit `app/iot_spark_jobs.py` for custom analyses
   - Add new job types as needed
   - Extend data processing logic

4. **Scale to Production**:
   - Deploy Flask to production WSGI server
   - Configure Spark for cluster mode
   - Integrate with real Spark cluster

## Support & Documentation

- **Flask**: https://flask.palletsprojects.com/
- **PySpark**: https://spark.apache.org/docs/latest/api/python/
- **Spark Web UI**: http://localhost:4040 (built-in)

---

**Status**: ✅ Ready for use  
**Last Updated**: December 9, 2025  
**Integration Level**: Complete (IoT + Spark)
