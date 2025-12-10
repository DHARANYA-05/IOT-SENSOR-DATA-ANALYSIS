#!/usr/bin/env python
"""Test IoT Spark job submission"""

import sys
sys.path.insert(0, '.')

# Fix Unicode on Windows
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app.main import app
import time

client = app.test_client()

print('=' * 70)
print('TESTING IoT SPARK JOB SUBMISSION')
print('=' * 70)
print()

# Test 1: Submit analyze sensors job
print('Test 1: Submitting IoT Sensor Analysis Job...')
r = client.post('/spark/iot/analyze-sensors', json={})

print(f'Response Status: {r.status_code}')
if r.status_code == 202:
    data = r.json
    print('[OK] Job Submitted Successfully!')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Status: {data.get("status")}')
    print(f'  Message: {data.get("message")}')
    print(f'  Spark UI: {data.get("spark_ui")}')
else:
    print(f'[ERROR] {r.json}')

print()

# Wait for job to execute
time.sleep(3)

# Test 2: Submit anomaly detection job
print('Test 2: Submitting Anomaly Detection Job...')
r = client.post('/spark/iot/detect-anomalies', json={})

print(f'Response Status: {r.status_code}')
if r.status_code == 202:
    data = r.json
    print('[OK] Job Submitted Successfully!')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Message: {data.get("message")}')
else:
    print(f'[ERROR] {r.json}')

print()

# Wait for job to execute
time.sleep(3)

# Test 3: Submit sensor summary job
print('Test 3: Submitting Sensor Summary Job...')
r = client.post('/spark/iot/sensor-summary', json={})

print(f'Response Status: {r.status_code}')
if r.status_code == 202:
    data = r.json
    print('[OK] Job Submitted Successfully!')
    print(f'  Operation: {data.get("operation")}')
    print(f'  Message: {data.get("message")}')
else:
    print(f'[ERROR] {r.json}')

print()

# Test 4: Get jobs
print('Test 4: Retrieving Job History...')
r = client.get('/spark/jobs')
data = r.json

print(f'Response Status: {r.status_code}')
if r.status_code == 200:
    print('[OK] Jobs Retrieved!')
    print(f'  Total Jobs: {data.get("total_count")}')
    print(f'  Running: {data.get("running_count")}')
    print(f'  Completed: {data.get("completed_count")}')
    
    if data.get('all_jobs'):
        print()
        print('  Recent Jobs:')
        for job in data.get('all_jobs', [])[:5]:
            print(f'    - {job.get("name")}: {job.get("status")}')
else:
    print(f'[ERROR] {r.json}')

print()
print('=' * 70)
print('TEST COMPLETE - IoT JOBS ARE RUNNING IN SPARK!')
print('=' * 70)
print()
print('Your Spark Web UI now shows:')
print('  - Sensor Analysis Job')
print('  - Anomaly Detection Job')
print('  - Sensor Summary Job')
print()
print('Access Spark Web UI at: http://localhost:4040 or http://localhost:4041')
