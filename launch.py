#!/usr/bin/env python
"""IoT Analytics Server - Ultra-Reliable Startup"""

import sys
import os
from pathlib import Path

# Setup paths
sys.path.insert(0, str(Path(__file__).parent))
os.chdir(str(Path(__file__).parent))

print("\n" + "="*70)
print("IoT Analytics - Starting Server")
print("="*70 + "\n")

try:
    # Load Flask app
    print("[1/2] Loading Flask application...")
    from app.main import app
    
    # Count routes
    route_count = len(list(app.url_map.iter_rules()))
    print(f"      READY: {route_count} routes configured")
    
    # Start server with Flask (no signal handling issues on Windows)
    print("[2/2] Starting Flask development server...")
    
    print("\n" + "="*70)
    print("SERVER LISTENING: http://127.0.0.1:5000")
    print("="*70)
    print("\nEndpoints:")
    print("  Dashboard:       http://127.0.0.1:5000/")
    print("  Sensors API:     http://127.0.0.1:5000/sensors")
    print("  Spark Status:    http://127.0.0.1:5000/spark/status")
    print("  Spark Dashboard: http://127.0.0.1:5000/spark-dashboard")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )

except KeyboardInterrupt:
    print("\n\nServer stopped")
    sys.exit(0)
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
