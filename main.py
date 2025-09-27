import datetime
import calendar

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

def main():
    print("Learner's Permit Validity Tracker")
    print("--------------------------------")
    
    # Set current date (hardcoded for Sep 27, 2025, as per provided context)
    current_date = datetime.date(2025, 9, 27)
    
    # Get issue date input
    while True:
        issue_str = input("Enter the date you got your learner's permit (YYYY-MM-DD): ")
        try:
            issue_date = datetime.datetime.strptime(issue_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Get validity period input
    while True:
        try:
            validity_months = int(input("Enter the validity period in months: "))
            if validity_months <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer for months.")
    
    # Calculate expiration
    expiration_date = add_months(issue_date, validity_months)
    
    # Check permit status
    status = check_permit_status(issue_date, expiration_date, current_date)
    
    # Output result
    print(f"\nYour learner's permit was issued on: {issue_date}")
    print(f"Validity period: {validity_months} months")
    print(f"It will expire on: {expiration_date}")
    print(f"Permit status as of {current_date}: {status}")

if __name__ == "__main__":
    main()