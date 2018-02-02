#James Roth
#2/2/18
#warmup4.py - "buzz" game

num=int(input("Enter a number: "))
if num.count(7)>0 or num%7==0:
    print("Buzz")
else:
    print(num)
