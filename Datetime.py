'''
    Update Note: Comment style changed.
'''
from datetime import datetime

# Now Date and Time
now = datetime.now()
print(now)

# Create Date
day = datetime(2017,3,3,13,33,0,0)
print(day)

# Datetime properties
print(day.year)
print(day.month)
print(day.day)
print(day.hour)
print(day.minute)
print(day.second)
print(day.microsecond)


# Unix Timestamp
print(day.timestamp())

# Example Time Difference
print(day.timestamp() - now.timestamp())

# Import date or time
from datetime import date, time

# Create date without time
normalday = date(2017,3,13)
print(normalday)

# Create time without date
normaltime = time(13,33,33)
print(normaltime)

# Combine date and time
combineddate = datetime.combine(normalday, normaltime)
print(combineddate)

# Datetime Formating
formattedDatetime = now.strftime("%d.%m.%Y")
print(formattedDatetime)

# Add new days, hours etc..
# Import timedelta
from datetime import timedelta
afterAdding = now + timedelta(days=3, hours=3, minutes=3, seconds=1)
print(afterAdding)

# Time Diffrent Calculation
day = datetime(2017,8,20)
td = now - day
print(td)
























