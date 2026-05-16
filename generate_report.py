import csv
from datetime import date, timedelta
import random

today = date.today()
filename = f"weekly_report_{today.isoformat()}.csv"

rows = []
for i in range(7):
    day = today - timedelta(days=i)
    rows.append({
        "day": day.isoformat(),
        "visitors": random.randint(80, 300),
        "signups": random.randint(2, 40),
    })

with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["day", "visitors", "signups"])
    writer.writeheader()
    for row in reversed(rows):
        writer.writerow(row)

print(f"Generated {filename} with {len(rows)} rows")