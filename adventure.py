#James Roth
#1/31/18
#adventure.py - nested conditional statements

print("You wake up in the middle of a dense forest. You look around and see an old path behind you, a tall tree to your right, and a dark cave to your left.")
choice=int(input("Press 1 to follow the path, press 2 to climb the tall tree to look around, and press 3 to explore the cave." ))

if choice==1:
    print("You follow the path for hours. It's hot, buggy, humid, and miserable, and the dense undergrowth eventually slows your progess to a mere crawl. ")
    choice=int(input("Do you keep folowing the path (1), or do you turn back and try to get back where you started? (2) "))
    