<#
One-click runner for the IoT Spark web app (pandas fallback).

What it does:
- Creates a venv if missing
- Installs Flask and pandas into the venv (small packages)
- Generates a large dataset if not present
- Starts the Flask app bound to 127.0.0.1:8080 in a new window
- Opens Chrome to the dashboard

Usage: Run this script from the project root in PowerShell (as your user):
    .\run_all.ps1

Note: If your environment requires a proxy for pip, set $env:HTTP_PROXY and $env:HTTPS_PROXY before running.
#>

Set-StrictMode -Version Latest

$venv = Join-Path $PWD '.venv'
$python = Join-Path $venv 'Scripts\python.exe'
$pip = Join-Path $venv 'Scripts\pip.exe'

if (-not (Test-Path $venv)) {
    Write-Host "Creating virtualenv..."
    python -m venv .venv
}

Write-Host "Installing required Python packages (Flask, pandas)..."
& $pip install --upgrade pip
& $pip install Flask pandas --disable-pip-version-check

# Generate dataset if missing
$dataset = Join-Path $PWD 'data\sensor_data_100k.csv'
if (-not (Test-Path $dataset)) {
    Write-Host "Generating dataset (100k rows)..."
    & $python .\data\generate_dataset.py --rows 100000 --sensors 200 --out sensor_data_100k.csv
} else {
    Write-Host "Dataset already exists: $dataset"
}

Write-Host "Starting Flask app (will bind to 127.0.0.1:8080)..."
# Start app in a new PowerShell window so it continues running after this script exits
Start-Process -FilePath $python -ArgumentList '.\app\main.py' -WorkingDirectory $PWD -WindowStyle Normal

Start-Sleep -Seconds 2
Write-Host "Opening Chrome at http://127.0.0.1:8080"
Start-Process "chrome.exe" "http://127.0.0.1:8080"

Write-Host "Done. If Chrome didn't open, run Start-Process 'chrome.exe' 'http://127.0.0.1:8080' manually."
