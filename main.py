from datetime import datetime

date = datetime.fromisoformat("2025-09-25T02:30")
datenow = datetime.now()

print(datenow-date)