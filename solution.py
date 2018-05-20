from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

def check_passport_date(pass_date, date_bright):
    day_b, month_b, year_b = map(int, re.findall(r'\d+', date_bright))
    day_p, month_p, year_p = map(int, re.findall(r'\d+', pass_date))

    date_bright = datetime(year_b, month_b, day_b)
    pass_date = datetime(year_p, month_p, day_p)

    day_14 = date_bright + relativedelta(years=+14)
    day_21 = date_bright + relativedelta(years=+21)
    day_21_1 = date_bright + relativedelta(years=+21, months=+1)
    day_45 = date_bright + relativedelta(years=+45)
    day_45_1 = date_bright + relativedelta(years=+45, months=+1)

    if day_21_1 > pass_date > day_14 and day_21 > datetime.now():
        return True

    if day_45_1 > pass_date > day_21 and day_45 > datetime.now():
        return True

    if pass_date > day_45:
        return True

    return False
