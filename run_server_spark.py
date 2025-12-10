"""
Enhanced Flask Server with Spark Web UI Integration
Features:
- Spark session management with Web UI
- Comprehensive logging
- Graceful shutdown
- Health monitoring
"""

import sys
import os
import logging
import signal
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def setup_spark_environment():
    """Setup Spark environment variables if needed"""
    # Ensure Java is configured
    if 'JAVA_HOME' not in os.environ:
        logger.warning("JAVA_HOME not set - Spark may not work correctly")
        logger.info("Please set JAVA_HOME to your Java installation directory")
    
    # Configure Spark UI
    os.environ.setdefault('SPARK_UI_PORT', '4040')
    logger.info(f"Spark Web UI will be available at http://localhost:{os.environ['SPARK_UI_PORT']}")

def main():
    """Main server startup function"""
    try:
        logger.info("="*70)
        logger.info("🏭 Factory IoT Sensor Monitoring System with Spark Integration")
        logger.info("="*70)
        
        # Setup environment
        setup_spark_environment()
        
        # Import Flask app
        logger.info("Loading Flask application...")
        from app.main import app
        logger.info("✓ Flask application loaded")
        
        # Pre-initialize Spark session
        logger.info("Initializing Spark session...")
        from app.spark_config import SparkConfig
        spark = SparkConfig.get_spark_session()
        logger.info("✓ Spark session initialized successfully")
        
        # Get status
        status = SparkConfig.get_status()
        logger.info(f"Spark Status:")
        logger.info(f"  App ID: {status.get('app_id')}")
        logger.info(f"  Version: {status.get('version')}")
        logger.info(f"  Threads: {status.get('threads')}")
        
        # Try waitress
        try:
            from waitress import serve
            use_waitress = True
            logger.info("Using Waitress WSGI server")
        except ImportError:
            use_waitress = False
            logger.info("Using Flask development server")
        
        port = int(os.environ.get('PORT', 5000))
        host = '127.0.0.1'
        
        logger.info("="*70)
        logger.info("Server Configuration:")
        logger.info(f"  Dashboard:     http://{host}:{port}/")
        logger.info(f"  API:           http://{host}:{port}/sensors")
        logger.info(f"  Spark Status:  http://{host}:{port}/spark/status")
        logger.info(f"  Spark Web UI:  http://localhost:4040")
        logger.info("="*70)
        logger.info("Press Ctrl+C to stop the server")
        logger.info("="*70 + "\n")
        
        # Graceful shutdown handler
        def signal_handler(signum, frame):
            logger.info("\nShutdown signal received, stopping server...")
            SparkConfig.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Start server
        if use_waitress:
            serve(app, host=host, port=port, threads=4, _quiet=False)
        else:
            app.run(host=host, port=port, debug=False, use_reloader=False, threaded=True)
    
    except KeyboardInterrupt:
        logger.info("\nServer interrupted")
        sys.exit(0)
    except Exception as e:
        logger.error(f"ERROR: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Cleanup
        try:
            from app.spark_config import SparkConfig
            SparkConfig.stop()
        except:
            pass

if __name__ == '__main__':
    main()
