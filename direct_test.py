#!/usr/bin/env python
"""Test Flask endpoints using test client"""
import sys
sys.path.insert(0, 'c:\\spark project')

try:
    print("[*] Importing app...")
    from app.main import app
    print("[✓] App imported")
    
    print("\n[*] Creating test client...")
    with app.test_client() as client:
        print("[✓] Test client created")
        
        print("\n[*] Testing /sensors endpoint...")
        try:
            response = client.get('/sensors')
            print(f"[✓] Status: {response.status_code}")
            if response.status_code == 200:
                print(f"[✓] Response length: {len(response.data)} bytes")
                print(f"[✓] Data: {response.json}")
            else:
                print(f"[!] Error: {response.data}")
        except Exception as e:
            print(f"[✗] Exception: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
        
        print("\n[*] Testing / (index) endpoint...")
        try:
            response = client.get('/')
            print(f"[✓] Status: {response.status_code}")
            if response.status_code == 200:
                print(f"[✓] HTML returned ({len(response.data)} bytes)")
            else:
                print(f"[!] Error: {response.data[:200]}")
        except Exception as e:
            print(f"[✗] Exception: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()

except Exception as e:
    print(f"[✗] FATAL: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n[✓] All tests completed!")
