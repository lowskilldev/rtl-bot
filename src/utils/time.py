import calendar

from datetime import datetime, timedelta, date

from src.constants import GroupType

def add_month(dt: datetime):
    year = dt.year + dt.month // 12
    month = dt.month % 12 + 1

    new_date = date(year, month, day = min(dt.day, calendar.monthrange(year, month)[1]))

    return datetime.combine(new_date.today(), datetime.min.time())

def add_delta(dt: datetime, step: GroupType):
    if step == GroupType.DAY:
        return dt + timedelta(days=1)
    elif step == GroupType.HOUR:
        return dt + timedelta(hours=1)
    elif step == GroupType.MONTH:
        return add_month(dt)