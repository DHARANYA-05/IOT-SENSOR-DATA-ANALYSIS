# PowerShell helper to create venv and run the Flask app
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python .\app\main.py
