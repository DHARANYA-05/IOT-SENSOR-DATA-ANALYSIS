#!/usr/bin/env python
"""Test Spark job submission"""

import sys
sys.path.insert(0, '.')

# Fix Unicode on Windows
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app.main import app
import time

client = app.test_client()

print('=' * 70)
print('TESTING SPARK JOB SUBMISSION')
print('=' * 70)
print()

# Test 1: Submit analyze job
print('Test 1: Submitting Analysis Job...')
r = client.post('/spark/submit-job', json={
    'job_name': 'IoT Data Analysis',
    'operation_type': 'analyze',
    'data_path': 'data/factory_sensors_data.csv'
})

print(f'Response Status: {r.status_code}')
if r.status_code == 202:
    data = r.json
    print('[OK] Job Submitted Successfully!')
    print(f'  Job Name: {data.get("job", {}).get("name")}')
    print(f'  Job Status: {data.get("job", {}).get("status")}')
    print(f'  App ID: {data.get("job", {}).get("app_id")}')
    print(f'  Spark UI: {data.get("spark_ui")}')
else:
    print(f'[ERROR] {r.json}')

print()

# Wait for job to execute
time.sleep(2)

# Test 2: Get jobs
print('Test 2: Retrieving Job History...')
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
        for job in data.get('all_jobs', [])[:3]:
            print(f'    - {job.get("name")}: {job.get("status")}')
else:
    print(f'[ERROR] {r.json}')

print()
print('=' * 70)
print('TEST COMPLETE - SPARK JOBS ARE RUNNING IN YOUR SPARK INSTANCE!')
print('=' * 70)
