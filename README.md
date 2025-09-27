Learner's Permit Validity Tracker

Overview

This is a simple console-based Python application that helps users track the validity of their learner's permit. Users input the date they received their permit and the validity period (in months), and the app calculates and displays the expiration date.

Features





Accepts a permit issue date in YYYY-MM-DD format.



Accepts a validity period in months.



Calculates the expiration date, accounting for varying month lengths.



Includes input validation to handle incorrect date formats or invalid month inputs.



Outputs the issue date, validity period, and expiration date.

Requirements





Python 3.x (no external libraries required, uses built-in datetime and calendar modules).

Installation





Ensure Python 3 is installed on your system. You can download it from python.org.



Save the Python script (e.g., permit_tracker.py) to a directory of your choice.

Usage





Open a terminal or command prompt.



Navigate to the directory containing the script.



Run the script using:

python permit_tracker.py



Follow the prompts:





Enter the permit issue date in YYYY-MM-DD format (e.g., 2025-09-27).



Enter the validity period in months (e.g., 6 for 6 months).



The app will display:





The permit issue date.



The validity period.



The calculated expiration date.

Example Interaction

Learner's Permit Validity Tracker
--------------------------------
Enter the date you got your learner's permit (YYYY-MM-DD): 2025-09-27
Enter the validity period in months: 6

Your learner's permit was issued on: 2025-09-27
Validity period: 6 months
It will expire on: 2026-03-27

Notes





The app handles month-end dates correctly (e.g., adding 1 month to Jan 31 results in Feb 28 or Feb 29 in a leap year).



Invalid inputs (e.g., incorrect date formats or non-positive months) will prompt the user to retry.



This is a console-based app. Future enhancements could include a GUI, web interface, or email reminders.

License

This project is open-source and available under the MIT License.
