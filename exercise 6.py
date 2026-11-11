# make snake,water,gun game 

import random
comp=random.randint(0,2)
b=int(input("choose 0 for snake or 1 for water or 2 for gun : "))
if b==comp:
    print("draw")
elif b==0 and comp==2:
    print("you lose")
elif b>comp:
    print("you lose")
else:
    print("you won")
print(f"as computer choosed {comp}")