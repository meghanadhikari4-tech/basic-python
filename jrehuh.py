import random
print("FUN GAME :) ")
play=input("do you want to play a dice roll game?(yes/no): ")
if play== "yes":
    print("..WELCOME TO MY GAME..")
else:
    print("quit")
while True:
    roll=input("roll the die (yes/no):")
    if roll.lower()=="yes":
        number=random.randint (1,6)
        print(f"you rolled {number}")
    else:
        if roll.lower()=="no":
            print("quit")
            break


