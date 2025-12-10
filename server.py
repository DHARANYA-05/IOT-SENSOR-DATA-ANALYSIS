#!/usr/bin/env python
"""WSGI server using Python standard library with background Spark init"""

import sys
import os
from pathlib import Path
import threading
import time

os.chdir(Path(__file__).parent)
sys.path.insert(0, '.')

print("\nStarting IoT Analytics Server...")

# Pre-initialize Spark in background thread
def init_spark_bg():
    """Initialize Spark in background to avoid blocking"""
    try:
        print("  - Initializing Spark in background...")
        from app.spark_config import SparkConfig
        spark = SparkConfig.get_spark_session()
        status = "READY" if SparkConfig._use_spark else "FALLBACK"
        print(f"  - Spark initialization: {status}")
    except Exception as e:
        print(f"  - Spark init warning: {e}")

spark_init_thread = threading.Thread(target=init_spark_bg, daemon=True)
spark_init_thread.start()

from app.main import app
from wsgiref.simple_server import make_server

print("Routes configured:", len(list(app.url_map.iter_rules())))
print("\nListening on http://127.0.0.1:5000\n")
print("Press Ctrl+C to stop\n")

server = make_server('127.0.0.1', 5000, app)
server.serve_forever()

