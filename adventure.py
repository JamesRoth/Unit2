print("Hello, world.")#James Roth
#1/31/18
#adventure.py - nested conditional statements

print("You wake up in the middle of a dense forest. You look around and see an old path behind you, a tall tree to your right, and a dark cave to your left.")
choice=int(input("Press 1 to follow the path, press 2 to climb the tall tree to look around, and press 3 to explore the cave." ))

if choice==1:
    print("You follow the path for hours. It's hot, buggy, humid, and miserable, and the dense undergrowth eventually slows your progess to a mere crawl. ")
    choice=int(input("Do you keep folowing the path (1), or do you turn back and try to get back where you started? (2) "))
    if choice==1:
        print(" ")

elif choice==2:
    print("It's a tough climb. The tree is covered in vines and slippery, decomposing leaves. Eventually, after much effort and a few close calls, you get to the top. Apparently you climbed the tallest tree in the jungle, and you're affored an unspoiled view of the surrounding land. However, you see a storm coming in and its inevitable rain will make the already dangerous climb down even worse, and the storm is almost on top of you. However, you've had no time to get your bearings and figure out where to go, and leaving the tree now would make the whole trip worthless. How long do you stay up in the tree?")
    choice=int(input("Before climing down, do you look around for 5 (1), 10 (2), or 15 (3) minutes? "))
    
    if choice==1:
        print("")
    elif choice==2:
        print(" ")
        
    else:
        print("You've made a mistake. The wind beats down you with surprising force, and the rain is coming down in torrents. Since the tree is so high, you're in the worst of the wind too. A climb down would be almost suicidal, but so would be staying in the tree.")
        choice=int(input("Do you wait out the storm (1), or climb down during it (2)? "))
        
        if choice==1:
            print("While waiting, a gust of wind catches you in the chest. You're thrown from the tree and you crash to the forest floor. You've died" )
        

else:
    print("You step gingerly toward the damp, dark cave. Every bad story you've ever heard would imply that this is a very bad idea. But, your options are limited and, at the very least, the cave would be a good shelter for the night.")
    choice=int(input("Do you enter the cave (1), or decide to play it safe and leave it alone (2) ? "))
    
    if choice==1:
        print(" ")
    else:
        print("Upon stepping into the cave, you notice is dead ends quickly. However, in a corner lies a tarp and a box presumably conatining some supplies. Seems like another person had the same idea you did. It now appears that this person has only recently vacated the cave, and the ashes of a fire are still warm. Should your rifle through their stuff or leave it alone?")
        choice=int(input("Do you touch the stuff (1), or leave it alone (2) ? "))
        
        if choice==1:
            print("While pilfering the supplies, you hear rustling in the bushes. All of a sudden a man is behind you. ""Who are you, and what are you doing?"", he says.")
            choice=int(input("You you lie (1), or tell the truth (2)?"))
