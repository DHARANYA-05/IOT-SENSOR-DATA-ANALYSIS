#!/usr/bin/env python
"""Test all sensor endpoints"""
import requests
import json

base_url = "http://127.0.0.1:5000"

print("\n[TEST 1] Get all sensors")
r = requests.get(f"{base_url}/sensors")
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"✓ Returned {len(data['sensors'])} sensors")
    print(f"First sensor: {json.dumps(data['sensors'][0], indent=2)}")
else:
    print(f"✗ Error: {r.text[:200]}")

if r.status_code == 200 and data['sensors']:
    sensor_id = data['sensors'][0]['sensor_id']
    
    print(f"\n[TEST 2] Get sensor details: {sensor_id}")
    r = requests.get(f"{base_url}/sensor/{sensor_id}")
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        detail = r.json()
        print(f"✓ Metadata: {json.dumps(detail['metadata'], indent=2)}")
        print(f"✓ Anomalies found: {len(detail['anomalies'])}")
    else:
        print(f"✗ Error: {r.text[:200]}")
    
    print(f"\n[TEST 3] Get sensor data: {sensor_id}")
    r = requests.get(f"{base_url}/data?sensor_id={sensor_id}")
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data_response = r.json()
        print(f"✓ Data points: {len(data_response['data'])}")
        if data_response['data']:
            print(f"Sample: {json.dumps(data_response['data'][0], indent=2)}")
    else:
        print(f"✗ Error: {r.text[:200]}")
    
    print(f"\n[TEST 4] Get anomalies for sensor: {sensor_id}")
    r = requests.get(f"{base_url}/anomalies?sensor_id={sensor_id}")
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        anomalies = r.json()
        print(f"✓ Anomalies: {len(anomalies['alerts'])}")
        if anomalies['alerts']:
            print(f"Sample: {json.dumps(anomalies['alerts'][0], indent=2)}")
    else:
        print(f"✗ Error: {r.text[:200]}")

print("\n[TEST 5] Server info")
r = requests.get(f"{base_url}/info")
print(f"Status: {r.status_code}")
if r.status_code == 200:
    info = r.json()
    print(f"✓ Backend: {info['backend']}")
    print(f"✓ Dataset: {info['dataset']}")
    print(f"✓ Rows: {info['rows']}")
else:
    print(f"✗ Error: {r.text[:200]}")

print("\n✓ All tests completed!")
