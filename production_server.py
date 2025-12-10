#!/usr/bin/env python
"""
IoT Analytics Server - Production Setup
Properly handles Flask app with all modules
"""

import sys
import os
import logging
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

# Configure logging to suppress verbose warnings
logging.basicConfig(
    level=logging.WARNING,
    format='%(message)s'
)
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('flask').setLevel(logging.ERROR)

print("\n" + "="*60)
print(">> IoT Analytics Platform - Starting Server")
print("="*60 + "\n")

try:
    # Import the Flask app
    print("[1/3] Loading application modules...")
    from app.main import app
    print("      OK - Flask app loaded")
    
    print("[2/3] Validating configuration...")
    routes_count = len(list(app.url_map.iter_rules()))
    print(f"      OK - {routes_count} routes configured")
    
    print("[3/3] Starting Waitress WSGI server...")
    
    from waitress import serve
    
    HOST = '127.0.0.1'
    PORT = 5000
    
    print(f"\n{'='*60}")
    print(f"OK - Server listening on http://{HOST}:{PORT}")
    print(f"{'='*60}\n")
    print("Available endpoints:")
    print(f"  * Dashboard:       http://{HOST}:{PORT}/")
    print(f"  * Sensors API:     http://{HOST}:{PORT}/sensors")
    print(f"  * Spark Status:    http://{HOST}:{PORT}/spark/status")
    print(f"  * Spark Monitor:   http://{HOST}:{PORT}/spark-dashboard")
    print(f"\n{'='*60}")
    print("Press Ctrl+C to stop\n")
    
    # Start the server
    serve(app, host=HOST, port=PORT, threads=4)

except KeyboardInterrupt:
    print("\nOK - Server stopped by user")
    sys.exit(0)
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
