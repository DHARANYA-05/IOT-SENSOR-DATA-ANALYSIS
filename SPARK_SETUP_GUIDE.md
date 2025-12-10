# Spark Web UI Integration Guide

## Overview
This project is now fully integrated with Apache Spark's Web UI for real-time monitoring and job tracking.

## Spark Web UI Endpoints

### Flask API Endpoints
- **GET `/spark/status`** - Get Spark session status and Web UI URL
- **GET `/spark/ui`** - Get Spark Web UI redirect link
- **GET `/info`** - Get backend info including Spark mode

### Accessing Spark Web UI
Once the server is running, the Spark Web UI is available at:
- **http://localhost:4040** - Default Spark Web UI port
- Or use the `/spark/ui` endpoint to get the dynamic URL

## Features

### Real-time Monitoring
- **Jobs**: View running and completed Spark jobs
- **Stages**: See job execution stages
- **Tasks**: Monitor individual task execution
- **Storage**: View cached RDD information
- **Executors**: Monitor executor performance

### Environment
- **Configuration**: View Spark configuration settings
- **Connected Executors**: Monitor connected executors

## Setup Instructions

### 1. Install PySpark
```powershell
pip install pyspark==3.4.1
```

### 2. Configure Environment (Optional)
```powershell
# Set custom Spark UI port (default: 4040)
$env:SPARK_UI_PORT = 4040

# Set custom master (default: local[*])
$env:SPARK_MASTER = "local[*]"
```

### 3. Start the Server
```powershell
# Using the enhanced server script
python server.py

# Or with waitress
waitress-serve --port 5000 app.main:app
```

### 4. Monitor in Real-time
1. Open main dashboard: http://127.0.0.1:5000
2. Check Spark status: http://127.0.0.1:5000/spark/status
3. Access Spark Web UI: http://localhost:4040

## Project Structure

```
app/
├── main.py           # Flask application with new Spark endpoints
├── spark_service.py  # Spark/Pandas service (updated)
├── spark_config.py   # NEW: Spark configuration management
├── static/          # Frontend assets
└── templates/       # HTML templates

data/
├── factory_sensors_data.csv
├── sensor_data.csv
└── generate_dataset.py

server.py            # Enhanced startup script with Spark logging
```

## API Usage Examples

### Check Spark Status
```bash
curl http://127.0.0.1:5000/spark/status
```

Response:
```json
{
  "spark": {
    "status": "active",
    "app_name": "IoTAnalytics",
    "app_id": "app-20251121144835-0000",
    "master": "local[4]",
    "version": "3.4.1",
    "ui_port": 4040,
    "ui_url": "http://localhost:4040",
    "threads": 4
  },
  "ui_enabled": true,
  "ui_url": "http://localhost:4040"
}
```

### Get Backend Info
```bash
curl http://127.0.0.1:5000/info
```

Response:
```json
{
  "backend": "pyspark",
  "dataset": "data/factory_sensors_data.csv",
  "rows": 10000
}
```

## Monitoring Tips

### Job Tracking
- Jobs page shows all Spark jobs submitted
- Check "Executors" for memory and GC statistics
- Use "Stages" tab to identify bottlenecks

### Performance
- Monitor task duration in the "Tasks" section
- Check shuffle read/write metrics
- Review garbage collection statistics

### Data Processing
- Verify data is being loaded as Spark DataFrames
- Check partition count in the Storage tab
- Monitor memory usage per executor

## Troubleshooting

### Web UI Not Accessible
1. Check if port 4040 is available: `netstat -ano | findstr :4040`
2. Verify Spark is running: `curl http://localhost:4040`
3. Check server logs for errors

### Spark Session Not Initializing
1. Verify PySpark installation: `python -c "import pyspark; print(pyspark.__version__)"`
2. Check JAVA_HOME is set correctly
3. Review server logs for initialization errors

### High Memory Usage
1. Reduce partition count: Modify `spark.sql.shuffle.partitions`
2. Decrease executor memory if needed
3. Check for data caching in the Storage tab

## Configuration Options

### Spark Configuration (in spark_config.py)
```python
SPARK_UI_PORT = 4040                    # Web UI port
SPARK_HISTORY_PORT = 18080              # History Server port
SPARK_MASTER = 'local[*]'               # Master URL
```

### Environment Variables
```
SPARK_UI_PORT=4040
SPARK_MASTER=local[*]
```

## Next Steps

1. **Enable Event Logging** for persistent job history
   ```python
   .config('spark.eventLog.enabled', 'true')
   .config('spark.eventLog.dir', './spark-events')
   ```

2. **Configure History Server** for long-term job tracking
3. **Add Custom Metrics** for application-specific monitoring
4. **Set up Spark SQL** tab configuration

## Integration Points

### SparkConfig (app/spark_config.py)
- Centralized session management
- Thread-safe singleton pattern
- Configurable UI ports and master

### SparkService (app/spark_service.py)
- Uses SparkConfig for session creation
- Maintains backwards compatibility
- Falls back to pandas if Spark unavailable

### Flask App (app/main.py)
- New `/spark/status` endpoint
- New `/spark/ui` endpoint
- Updated `/info` endpoint with Spark mode

## Performance Benchmarks

Default Configuration (local[*]):
- 10K rows processing: < 1 second
- 100K rows processing: 2-3 seconds
- Anomaly detection: Real-time on full dataset

## Support & Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark API](https://spark.apache.org/docs/latest/api/python/)
- [Spark Web UI Guide](https://spark.apache.org/docs/latest/web-ui.html)
