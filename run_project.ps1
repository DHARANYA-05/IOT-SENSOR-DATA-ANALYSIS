# ============================================================
# IoT Analytics + Spark Web UI Project Launcher (PowerShell)
# ============================================================
# This script starts your complete IoT project with Spark integration

Write-Host ""
Write-Host "============================================================"
Write-Host "IoT Analytics + Spark Web UI - Project Launcher"
Write-Host "============================================================"
Write-Host ""

# Kill any existing Python processes
Write-Host "Cleaning up old processes..."
taskkill /FI "IMAGENAME eq python.exe" /F 2>&1 | Out-Null
Start-Sleep -Seconds 2

# Navigate to project directory
Set-Location "c:\spark project"

# Start server
Write-Host "Starting Flask server with Spark integration..."
Write-Host ""
Write-Host "Server will start on: http://127.0.0.1:5000"
Write-Host ""

.\.venv\Scripts\python.exe server.py
