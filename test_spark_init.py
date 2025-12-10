#!/usr/bin/env python
"""Test Spark session initialization"""

import sys
sys.path.insert(0, '.')

from app.spark_config import SparkConfig

print('=' * 70)
print('TESTING SPARK SESSION INITIALIZATION')
print('=' * 70)
print()

try:
    spark = SparkConfig.get_spark_session()
    print('[OK] Spark Session Created Successfully!')
    print()
    print('Session Information:')
    print(f'  App Name: {getattr(spark, "appName", "N/A")}')
    print(f'  App ID: {getattr(spark, "appId", "N/A")}')
    print(f'  Master: {getattr(spark, "master", "N/A")}')
    print(f'  Version: {getattr(spark, "version", "N/A")}')
    print(f'  Using Real Spark: {SparkConfig._use_spark}')
    print()
    
    status = SparkConfig.get_status()
    print('Spark Status:')
    print(f'  UI URL: {status.get("ui_url")}')
    print(f'  Backend: {status.get("backend")}')
    print(f'  Status: {status.get("status")}')
    print()
    
    if SparkConfig._use_spark:
        print('[OK] Real Spark is available!')
        print(f'  Access Spark Web UI at: {status.get("ui_url")}')
    else:
        print('[WARN] Using fallback Pandas mode')
        print('  (Spark not available, but mock jobs will work)')
    
    print()
    print('=' * 70)
    
except Exception as e:
    print(f'[ERROR] Error: {e}')
    import traceback
    traceback.print_exc()
