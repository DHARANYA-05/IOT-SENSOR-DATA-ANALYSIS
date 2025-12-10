#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test Spark integration setup"""

import sys
import os

# Set UTF-8 encoding for Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'

sys.path.insert(0, 'c:\\spark project')
print('Testing Spark integration...')
print()

try:
    from app.spark_config import SparkConfig
    print('[OK] SparkConfig imported')
    
    spark = SparkConfig.get_spark_session()
    print('[OK] Spark session created')
    
    status = SparkConfig.get_status()
    st = status['status']
    appid = status['app_id']
    uiurl = status['ui_url']
    appname = status['app_name']
    print(f'[OK] Spark Status: {st}')
    print(f'     App Name: {appname}')
    print(f'     App ID: {appid}')
    print(f'     Web UI: {uiurl}')
    print()
    
    # Test data loading
    from app.spark_service import SparkService
    service = SparkService.create()
    print('[OK] SparkService created')
    
    df = service.load_csv('data/factory_sensors_data.csv')
    count = df.count()
    cols = len(df.columns)
    print(f'[OK] CSV loaded as Spark DataFrame')
    print(f'     Rows: {count}')
    print(f'     Columns: {cols}')
    print()
    
    print('[SUCCESS] All Spark components working correctly!')
    
except Exception as e:
    print(f'[ERROR] {e}')
    import traceback
    traceback.print_exc()
