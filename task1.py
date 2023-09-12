import datetime as dt
from dateutil.relativedelta import relativedelta


current_date = dt.datetime.now()
x = current_date + relativedelta(days = -15)
y = x.strftime("%d-%m-%Y")
print(y)
