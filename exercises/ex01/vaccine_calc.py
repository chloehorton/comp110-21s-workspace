"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vacc: int = int(input("Target percent vaccinated: "))
days_till_vacc: int = round(((pop * (target_percent_vacc / 100 )) - (doses_admin / 2)) / (doses_per_day / 2))
today: datetime = datetime.today()
days_added: timedelta = timedelta(days_till_vacc)
date: datetime = today + days_added

print("We will reach " + str(target_percent_vacc) + "% vaccination in " + str(days_till_vacc) + " days, which falls on " + str(date.strftime("%B %d, %Y")))
