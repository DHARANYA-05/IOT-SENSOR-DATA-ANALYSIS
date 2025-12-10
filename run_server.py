#!/usr/bin/env python
import sys
import os
import signal

def signal_handler(sig, frame):
    print('\n[!] Received interrupt signal')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    print("[*] Importing Flask app...")
    from app.main import app
    print("[✓] App imported successfully")
    
    print("[*] Starting Flask server...")
    print("[*] Open browser to: http://127.0.0.1:5000")
    print("[*] Press Ctrl+C to stop\n")
    
    # Force use_reloader=False to prevent subprocess spawning issues
    # Add threaded=True for stability
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )
    print("[!] app.run() returned")
    
except KeyboardInterrupt:
    print("\n[!] Server stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"\n[ERROR] {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    print("[*] Cleanup complete")
