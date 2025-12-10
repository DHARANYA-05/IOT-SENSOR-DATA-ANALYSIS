#!/usr/bin/env python
"""Production Flask Server with Spark Web UI"""

import sys
import os
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
os.chdir(str(project_root))

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 FACTORY IoT SENSOR MONITORING SYSTEM")
    print("="*70)
    
    try:
        print("\n[1/3] Loading Flask application...")
        from app.main import app
        print("      ✓ Flask app loaded")
        
        print("[2/3] Loading Spark configuration...")
        # Skip direct Spark init to avoid background Java processes
        # Spark will be initialized lazily when needed
        print("      ✓ Spark configured (pandas mode)")
        
        print("[3/3] Starting Waitress server...\n")
        from waitress import serve
        
        print("="*70)
        print("📊 DASHBOARD & API ENDPOINTS:")
        print("="*70)
        print("  Web UI:        http://127.0.0.1:5000/")
        print("  Sensors API:   http://127.0.0.1:5000/sensors")
        print("  Spark Status:  http://127.0.0.1:5000/spark/status")
        print("  Spark Monitor: http://127.0.0.1:5000/spark-dashboard")
        print("="*70)
        print("\nServer running... Press Ctrl+C to stop\n")
        
        serve(app, host='127.0.0.1', port=5000, threads=4, _quiet=False)
        
    except KeyboardInterrupt:
        print("\n\n[✓] Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[✗] ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
