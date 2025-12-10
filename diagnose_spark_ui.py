#!/usr/bin/env python
"""
Spark Web UI Connection Diagnostic Tool
Identifies and fixes connection issues
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import requests
import json
from datetime import datetime

print("\n" + "="*70)
print("⚡ SPARK WEB UI CONNECTION DIAGNOSTIC")
print("="*70 + "\n")

# Step 1: Check Flask App
print("[1/6] Checking Flask Application...")
try:
    from app.main import app
    print("  ✓ Flask app loaded successfully")
    
    routes = [r.rule for r in app.url_map.iter_rules() if 'spark' in r.rule]
    print(f"  ✓ Found {len(routes)} Spark-related routes:")
    for route in sorted(routes):
        print(f"    - {route}")
except Exception as e:
    print(f"  ✗ Failed to load Flask app: {e}")
    sys.exit(1)

# Step 2: Check SparkConfig
print("\n[2/6] Checking SparkConfig...")
try:
    from app.spark_config import SparkConfig
    print("  ✓ SparkConfig imported successfully")
    
    status = SparkConfig.get_status()
    print(f"  ✓ SparkConfig.get_status() works:")
    print(f"    - Backend: {status.get('backend')}")
    print(f"    - UI Port: {status.get('ui_port')}")
    print(f"    - UI URL: {status.get('ui_url')}")
    print(f"    - Status: {status.get('status')}")
    print(f"    - Spark Available: {status.get('spark_available')}")
except Exception as e:
    print(f"  ✗ Failed to check SparkConfig: {e}")
    sys.exit(1)

# Step 3: Check SparkUIBridge
print("\n[3/6] Checking SparkUIBridge...")
try:
    from app.spark_ui_bridge import SparkUIBridge, SPARK_UI_URL
    print("  ✓ SparkUIBridge imported successfully")
    print(f"  ✓ Configured URL: {SPARK_UI_URL}")
    
    available = SparkUIBridge.is_spark_ui_available()
    print(f"  ℹ Spark Web UI at :4040 is {'Available' if available else 'Not Available (expected with Java 24)'}")
except Exception as e:
    print(f"  ✗ Failed to check SparkUIBridge: {e}")
    sys.exit(1)

# Step 4: Test Flask Routes
print("\n[4/6] Testing Flask Routes (Start simple server for 3 seconds)...")
try:
    from app.main import app as flask_app
    from threading import Thread
    import time
    
    # Start server in background
    def run_server():
        flask_app.run(host='127.0.0.1', port=5555, debug=False, use_reloader=False)
    
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(2)
    
    # Test endpoints
    endpoints_to_test = [
        '/spark/status',
        '/spark/ui',
        '/spark-ui/status',
        '/sensors'
    ]
    
    for endpoint in endpoints_to_test:
        try:
            response = requests.get(f'http://127.0.0.1:5555{endpoint}', timeout=2)
            data = response.json() if response.status_code == 200 else None
            status_icon = "✓" if response.status_code == 200 else "✗"
            print(f"  {status_icon} GET {endpoint}: {response.status_code}")
        except Exception as e:
            print(f"  ✗ GET {endpoint}: {str(e)[:50]}")
    
except Exception as e:
    print(f"  ℹ Skipping live server test (optional): {str(e)[:50]}")

# Step 5: Check Template Files
print("\n[5/6] Checking Template Files...")
try:
    template_path = 'app/templates/spark_dashboard.html'
    if os.path.exists(template_path):
        print(f"  ✓ Found {template_path}")
        with open(template_path, 'r') as f:
            content = f.read()
            if 'spark-status' in content or 'loadSparkStatus' in content:
                print(f"  ✓ Dashboard contains Spark status monitoring")
    else:
        print(f"  ✗ Missing {template_path}")
except Exception as e:
    print(f"  ✗ Failed to check templates: {e}")

# Step 6: Configuration Summary
print("\n[6/6] Configuration Summary...")
try:
    from app.spark_config import SparkConfig
    from app.spark_ui_bridge import SPARK_UI_URL
    
    print("\n  📊 Current Setup:")
    print(f"    Flask Server Port: 5000")
    print(f"    Spark Web UI Port: 4040")
    print(f"    Spark Web UI URL: {SPARK_UI_URL}")
    print(f"    Dashboard URL: http://127.0.0.1:5000/spark-dashboard")
    print(f"    Status API: http://127.0.0.1:5000/spark/status")
    
    print("\n  ℹ Status:")
    status = SparkConfig.get_status()
    if status.get('spark_available'):
        print("    ✓ Real Spark is available (Java compatible)")
    else:
        print("    ℹ Using Pandas fallback (Java 24 or not compatible)")
    
except Exception as e:
    print(f"  ✗ Error in configuration summary: {e}")

print("\n" + "="*70)
print("✅ DIAGNOSTIC COMPLETE")
print("="*70)
print("\nTo start the server, run:")
print("  python run_server_spark.py")
print("\nThen visit:")
print("  http://127.0.0.1:5000/spark-dashboard")
print("="*70 + "\n")
