import datetime

# Starting date
start_date = datetime.date.today() # October 26, 2025, 10:00:00

# Interval to add (e.g., 5 days, 3 hours, 15 minutes)
time_to_add = datetime.timedelta(days=5)

# Calculate the new date and time
end_date = start_date + time_to_add

print(f"Original date and time: {start_date}")
print(f"New date and time: {end_date}")