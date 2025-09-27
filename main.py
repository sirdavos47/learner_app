import datetime
import calendar
import json

def add_months(source_date, months):
    """
    Adds a given number of months to a date, handling month-end days properly.
    """
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

def check_permit_status(issue_date, expiration_date, current_date):
    """
    Checks if the permit is valid based on the current date.
    """
    if current_date <= expiration_date:
        return "Valid"
    else:
        return "Expired"

if __name__ == "__main__":
    main()