#!/usr/bin/env python
import sys
sys.path.insert(0, 'c:\\spark project')

from app.main import app

with app.test_client() as client:
    try:
        print("Testing /sensor/SENSOR_001...")
        response = client.get('/sensor/SENSOR_001')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json}")
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()
