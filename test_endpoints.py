#!/usr/bin/env python
import sys
import json
import traceback

try:
    print("[1/3] Importing Flask app...")
    from app.main import app
    print("✓ App imported")
    
    print("\n[2/3] Testing /sensors endpoint...")
    with app.test_client() as client:
        response = client.get('/sensors')
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = json.loads(response.data)
            print(f"✓ Sensors returned: {len(data['sensors'])}")
            print(f"First sensor: {data['sensors'][0]}")
        else:
            print(f"❌ Error: {response.data.decode()}")
    
    print("\n[3/3] Testing / (index) endpoint...")
    with app.test_client() as client:
        response = client.get('/')
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"✓ Index page rendered successfully ({len(response.data)} bytes)")
        else:
            print(f"❌ Error: {response.data.decode()[:200]}")
            
except Exception as e:
    print(f"\n❌ EXCEPTION: {type(e).__name__}")
    print(f"Message: {str(e)}")
    traceback.print_exc()
    sys.exit(1)

print("\n✓ All endpoint tests passed!")
