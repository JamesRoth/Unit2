#James Roth
#1/29/18
#unitConverter.py - converting units with if statements

convert=float(input("What would you like to convert? Enter 1 for KM to Miles, 2 for KG to LBS, 3 for Liters to Gallons, and 4 for Celsius to Fahrenheight."))
if convert==1:
    km=float(input("Enter amount of KM: "))
    print(km, "kilometers is", round(km*0.621371, 1), "miles.")
if convert==2:
    kg=float(input("Enter a number of kilograms: ")
    print(kg, "kilograms is", kg*2.20462, "pounds.")
if 
