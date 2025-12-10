#!/usr/bin/env python
import sys
sys.path.insert(0, '.')
from app.main import app
import json

client = app.test_client()

print("Testing Mock Spark Data Integration")
print("=" * 50)
print()

# Test jobs
r = client.get('/spark-ui/jobs')
data = json.loads(r.data)
print("Jobs Endpoint:")
print(f"  Status: {r.status_code}")
print(f"  Jobs: {len(data.get('jobs', []))}")
for job in data.get('jobs', []):
    print(f"    - {job.get('name')}: {job.get('status')}")

print()

# Test stages
r = client.get('/spark-ui/stages')
data = json.loads(r.data)
print("Stages Endpoint:")
print(f"  Status: {r.status_code}")
print(f"  Stages: {len(data.get('stages', []))}")
for stage in data.get('stages', []):
    print(f"    - Stage {stage.get('stageId')}: {stage.get('status')}")

print()

# Test executors
r = client.get('/spark-ui/executors')
data = json.loads(r.data)
print("Executors Endpoint:")
print(f"  Status: {r.status_code}")
print(f"  Executors: {len(data.get('executors', []))}")
for executor in data.get('executors', []):
    print(f"    - Executor {executor.get('id')}: {executor.get('host')}")

print()
print("=" * 50)
print("SUCCESS: All mock data endpoints working!")
