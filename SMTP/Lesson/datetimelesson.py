import datetime as dt

# How to get the current time

now = dt.datetime.now()
# datetime is a class. The method now returns current date and time
year = now.year # year is a string, while now is a date time object
# There is an attribute for every time unit




# How to make a datetime object of our own?

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)  # --> 1995-12-15 00:00:00






