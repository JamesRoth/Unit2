#James Roth
#2/12/18
#quiz2.py - if statements quiz

word1=input("Enter a word: ")
word2=input("Enter a word: ")

if len(word1)>len(word2):
    print(word1, "is longer than", word2)
elif len(word1)<len(word2):
    print(word1, "is shorter than", word2)
else:
    print(word1, "and", word2, "are the same length")

if "p" in word1 or word2:
    if "p" in word1 and "p" in word2:
        print("p is in", word1, "and", word2)
        
    elif "p" in word1:
        print("p is in", word1)
        
    elif "p" in word2:
        print("p is in", word2)
        
if "p" not in word1 or "p" not in word2:
    print("p is not in", word1, "or", word2)
    
num1=int(input("You will enter 2 numbers that add to 12. Enter the first one: "))
num2=int(input("Enter the second one: "))

