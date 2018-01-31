#James Roth
#1/31/18
#adventure.py - nested conditional statements

print("You wake up in the middle of a dense forest. You look around and see an old path behind you, a tall tree to your right, and a dark cave to your left.")
choice=int(input("Press 1 to follow the path, press 2 to climb the tall tree to look around, and press 3 to explore the cave." ))

if choice==1:
    print("You follow the path for hours. It's hot, buggy, humid, and miserable, and the dense undergrowth eventually slows your progess to a mere crawl. ")
    choice=int(input("Do you keep folowing the path (1), or do you turn back and try to get back where you started? (2) "))
    if choice==1:
        
    
    else:
        

elif choice==2:
    print("It's a tough climb. The tree is covered in vines and slippery, decomposing leaves. Eventually, after much effort and a few close calls, you get to the top. Apparently you climbed the tallest tree in the jungle, and you're affored an unspoiled view of the surrounding jungle. However, you see a storm coming in and its inevitable rain will make the already dangerous climb down even worse, and the storm is right on top of you. However, you've had no time to get your bearings and figure out where to go, and leaving the tree now would make the whole trip worthless. How long do you stay up in the tree?
    choice=int(input("Before climing down, do you look around for 5 (1), 10 (2), or 15 (3) minutes? "))
    
    if choice==1:
        
    elif choice==2:
        
    else:
        

else:
    print("You step gingerly toward the damp, dark cave. Everything bad 