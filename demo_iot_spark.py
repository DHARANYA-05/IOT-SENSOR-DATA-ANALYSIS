#!/usr/bin/env python
"""
Quick test to submit IoT Spark jobs and show execution
"""

import sys
sys.path.insert(0, '.')

import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app.main import app
import time
import json

client = app.test_client()

print('\n' + '='*80)
print('IoT PROJECT WITH SPARK WEB UI - DEMONSTRATION')
print('='*80)
print()

print('[1] Submitting Sensor Analysis Job to Spark...')
print('-' * 80)
r = client.post('/spark/iot/analyze-sensors', json={})
if r.status_code == 202:
    data = r.json
    print(f'  Status: {data.get("status").upper()}')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Message: {data.get("message")}')
    print(f'  Spark UI: {data.get("spark_ui")}')
    print()
    print('  >>> Job is now running in your Spark cluster!')
else:
    print(f'  ERROR: {r.json}')

time.sleep(2)

print()
print('[2] Submitting Anomaly Detection Job to Spark...')
print('-' * 80)
r = client.post('/spark/iot/detect-anomalies', json={})
if r.status_code == 202:
    data = r.json
    print(f'  Status: {data.get("status").upper()}')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Message: {data.get("message")}')
    print()
    print('  >>> Job is now running in your Spark cluster!')
else:
    print(f'  ERROR: {r.json}')

time.sleep(2)

print()
print('[3] Submitting Sensor Summary Job to Spark...')
print('-' * 80)
r = client.post('/spark/iot/sensor-summary', json={})
if r.status_code == 202:
    data = r.json
    print(f'  Status: {data.get("status").upper()}')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Message: {data.get("message")}')
    print()
    print('  >>> Job is now running in your Spark cluster!')
else:
    print(f'  ERROR: {r.json}')

print()
print('='*80)
print('APPLICATION STRUCTURE')
print('='*80)
print()
print('Your Flask Application:')
print('  - Main Dashboard: http://127.0.0.1:5000/')
print('  - Spark Jobs Control: http://127.0.0.1:5000/spark-jobs')
print('  - Integrated Dashboard: http://127.0.0.1:5000/integrated-dashboard')
print()
print('Your Spark Web UI:')
print('  - Jobs Page: http://localhost:4040 or http://localhost:4041')
print('  - Stages: http://localhost:4040/stages or http://localhost:4041/stages')
print('  - Executors: http://localhost:4040/executors or http://localhost:4041/executors')
print()
print('IoT Operations Endpoints:')
print('  - POST /spark/iot/analyze-sensors')
print('  - POST /spark/iot/detect-anomalies')
print('  - POST /spark/iot/sensor-summary')
print()
print('='*80)
print('READY TO USE!')
print('='*80)
print()
print('Next Steps:')
print('  1. Open http://127.0.0.1:5000/ in your browser')
print('  2. Navigate to Spark Jobs from the navbar')
print('  3. Click any IoT Operation button to submit a job')
print('  4. Watch it execute in the Spark Web UI')
print()
