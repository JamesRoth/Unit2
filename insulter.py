#James Roth
#1/30/18
#insulter.py - random ints and choosing statements

from random import randint

name=input("Enter your name: ")
insult=int(randint(1,5))
if insult==1:
    print("You have the brains of a dead fly.")
elif insult==2: 
    print("You're a waste of air.")
elif insult==3:
    print("Calling you worthless is an understatement.")
elif insult==4: 
    print("You're the definition of dissapointment.")
else:
    print("Cats are smarter than you.")

