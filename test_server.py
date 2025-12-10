#!/usr/bin/env python
"""Test and start Flask server with detailed diagnostics."""

import traceback
import sys
import os

os.chdir('c:\\spark project')
sys.path.insert(0, 'c:\\spark project')

try:
    print("[1/6] Importing Flask...")
    from flask import Flask
    print("      ✓ Flask imported")
    
    print("[2/6] Importing SparkService...")
    from app.spark_service import SparkService
    print("      ✓ SparkService imported")
    
    print("[3/6] Creating SparkService instance...")
    service = SparkService.create()
    print("      ✓ Service created")
    
    print("[4/6] Loading dataset...")
    df = service.load_csv('data/factory_sensors_data.csv')
    print(f"      ✓ Dataset loaded: {len(df)} rows")
    
    print("[5/6] Importing app.main...")
    from app.main import app
    print("      ✓ app.main imported")
    
    print("[6/6] Starting Flask server on http://127.0.0.1:5000...")
    print("=" * 70)
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"   Message: {e}")
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
