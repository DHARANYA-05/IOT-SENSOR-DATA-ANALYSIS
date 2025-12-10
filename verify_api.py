#!/usr/bin/env python
"""Direct test of sensor endpoints"""
import sys
sys.path.insert(0, 'c:\\spark project')

try:
    from app.main import app
    
    with app.test_client() as client:
        print("[TEST 1] List all sensors")
        r = client.get('/sensors')
        if r.status_code == 200:
            sensors = r.json['sensors']
            print(f"✓ Got {len(sensors)} sensors")
            print(f"First 3 sensors:")
            for s in sensors[:3]:
                print(f"  - {s['sensor_id']}: {s['machine']} ({s['type']})")
        else:
            print(f"✗ Error {r.status_code}: {r.data}")
        
        sensor_id = 'SENSOR_001'
        print(f"\n[TEST 2] Get details for {sensor_id}")
        r = client.get(f'/sensor/{sensor_id}')
        if r.status_code == 200:
            detail = r.json
            print(f"✓ Metadata: {detail['metadata']}")
            print(f"✓ Anomalies found: {len(detail['anomalies'])}")
        else:
            print(f"✗ Error {r.status_code}: {r.data}")
        
        print(f"\n[TEST 3] Get data for {sensor_id}")
        r = client.get(f'/data?sensor_id={sensor_id}')
        if r.status_code == 200:
            data = r.json['data']
            print(f"✓ Got {len(data)} data points")
            if data:
                print(f"  First point: {data[0]}")
                print(f"  Last point: {data[-1]}")
        else:
            print(f"✗ Error {r.status_code}: {r.data}")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
