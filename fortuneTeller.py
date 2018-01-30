#James Roth
#1/30/18
#fortuneTeller.py - different if statements

color=input("Pick a color: red or green: ")
num=int(input("Pick a number from 1-4: "))

if color=="red":
    if num==1:
        print("You will lose your pet fish.")
    elif num==2:
        print("You will break an arm.")
    elif num==3:
        print("You will win a car.")
    elif num==4:
        print("You will get struck by lightning.")
elif color=="blue":
    if num==1:
        print("You will get hit by a car.")
    elif num==2:
        print("You will win the lottery.")
    elif num==3:
        print("North Korea will invade the US.")
    elif num==4:
        print("The patriots will lose the super bowl.")
elif color !="red" and color !="blue" or num>4 or num<1:
    print("You cannot follow directions.")