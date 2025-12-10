#!/usr/bin/env python
"""Quick start Flask server"""
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

print("\n🚀 Starting IoT Analytics Server...\n")

from app.main import app
from waitress import serve

print("✓ Server ready on http://127.0.0.1:5000\n")

serve(app, host='127.0.0.1', port=5000, threads=4, _quiet=False)
