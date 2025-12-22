name=input("enter your name: ")
print("you are welcome to the game :) ")
answer=input("you are on aeroplane which is going to crash you have the option to wear parachuite and fly or have some safety measures")
if answer=="wear parachuite":
    print("you fly downwards but you have the option to fly towards river or towards ground" )
    if answer==input("fly towars river" ):
      print("you die!" )
else:
        print("you survived!" )
if answer=="have some safety measures":
    print("you sit inside the sofa and you survived" )
else:
    print("you die plz try again :( " )        