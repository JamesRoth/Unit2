#James Roth
#1/29/18
#gradeCalculator.py - if statements to calc grades

grade=int(input("Enter your grade: "))
if grade>89:
    print("You earned an A")
elif grade>79:
    print("You earned a B")
elif grade>69:
    print("You earned a C")
elif grade>59:
    print("You earned a D")
else:
    print("You earned an NC")