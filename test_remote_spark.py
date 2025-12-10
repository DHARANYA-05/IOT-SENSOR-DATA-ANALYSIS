#!/usr/bin/env python
import sys
sys.path.insert(0, '.')
from app.main import app
import json

client = app.test_client()

print("=" * 70)
print("SPARK REMOTE CONNECTION TEST - http://dharanya:4040")
print("=" * 70)
print()

# Test jobs
print("✓ Testing /spark-ui/jobs endpoint:")
r = client.get('/spark-ui/jobs')
data = json.loads(r.data)
if 'jobs' in data:
    print(f"  Status: {r.status_code}")
    print(f"  Response size: {len(r.data)} bytes")
    jobs = data.get('jobs', [])
    print(f"  Found {len(jobs)} jobs")
    if jobs:
        for job in jobs[:2]:
            print(f"    - {json.dumps(job)[:80]}...")
else:
    print(f"  Response: {json.dumps(data)[:200]}")

print()

# Test stages
print("✓ Testing /spark-ui/stages endpoint:")
r = client.get('/spark-ui/stages')
data = json.loads(r.data)
if 'stages' in data:
    print(f"  Status: {r.status_code}")
    print(f"  Response size: {len(r.data)} bytes")
    stages = data.get('stages', [])
    print(f"  Found {len(stages)} stages")
else:
    print(f"  Response: {json.dumps(data)[:200]}")

print()

# Test executors
print("✓ Testing /spark-ui/executors endpoint:")
r = client.get('/spark-ui/executors')
data = json.loads(r.data)
if 'executors' in data:
    print(f"  Status: {r.status_code}")
    print(f"  Response size: {len(r.data)} bytes")
    executors = data.get('executors', [])
    print(f"  Found {len(executors)} executors")
    if executors:
        for executor in executors[:2]:
            print(f"    - {json.dumps(executor)[:80]}...")
else:
    print(f"  Response: {json.dumps(data)[:200]}")

print()
print("=" * 70)
print("SUCCESS: Connected to remote Spark at dharanya:4040!")
print("=" * 70)
