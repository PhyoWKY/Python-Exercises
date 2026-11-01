# Dates and Times

import datetime

date = datetime.date(day=20, month=5, year=2026)
today = datetime.date.today()

time = datetime.time(hour=12, minute=30, second=00)
now = datetime.datetime.now() # The first 'datetime' is module, the second one is class, followed by 'now' method

now = now.strftime("%H:%M:%S %d-%m-%Y") # More info in 'datetime' documentation online

print(date)
print(today)
print(time)
print()
print(now)

print()

target_datetime = datetime.datetime(year=2030, month=1, day=2, hour=12, minute=30, second=1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")