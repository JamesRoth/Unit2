#James Roth
#2/5/18
#ageCalculator.py - age and current date

from datetime import date

year=int(input("Enter the year you were born: "))
month=int(input("Enter the month you were born: "))
day=int(input("Enter the day you were born: "))

if date.today().month==month and date.today().day==day:
    print("Happy birthday!")
if date.today().month<=month:
    if date.today().day<day:
        print("You are", date.today().year-(year+1), "years old.")
    else: 
        print("You are", date.today().year-year, "years old.")
    