import datetime as dt
from dateutil.relativedelta import relativedelta
reminder_message = "Hello Friedrich, your rent of 300 € is due on "
current_date = dt.datetime(year=2020, month=1, day=1)
x = current_date + relativedelta(days = 5)
y = x.strftime("%d-%m-%Y")
print(reminder_message + str(y) )