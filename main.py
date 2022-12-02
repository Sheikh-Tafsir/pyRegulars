import random

thislist = ["apple", "banana", "cherry", "pineapple", "berry", "cherry", "melon"];
i=7
j=0
while i>0:
    n = random.randint(0, 4)
    if n==1:
        j=j+1
        i=i-1;
        print(thislist[j:7])
        print()
