#!/usr/bin/env python
"""Flask development server"""
import sys
import os
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
os.environ['FLASK_ENV'] = 'production'

# Suppress Flask warnings
logging.getLogger('werkzeug').setLevel(logging.ERROR)

print("\n🚀 Starting IoT Analytics Server...\n")

try:
    from app.main import app
    print("✓ Flask app loaded")
    print("✓ Running on http://127.0.0.1:5000\n")
    print("Press Ctrl+C to stop\n")
    
    app.run(
        host='127.0.0.1', 
        port=5000, 
        debug=False, 
        use_reloader=False, 
        threaded=True,
        use_evalex=False
    )
except KeyboardInterrupt:
    print("\n✓ Server stopped")
    sys.exit(0)
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
