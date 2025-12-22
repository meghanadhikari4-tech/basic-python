print("welcome to my quiz game")
playing=input("do you want to play? ")
if playing.lower() != "yes" :
    quit()

print("continue playing :) ")
score=0

ques1=input("what is your name? ")
if ques1.lower() == "meghan":
  print("you are right!")
  score +=1
else:
   print("please try again :( ")

ques2=input("what is our national animal? ")
if ques2.lower()=="cow":
   print("you are right!")
   score +=2
else:
   print("sorry try again :( ")

ques3=input("what is your favourite food? ")
if ques3.lower()=="momo":
   print("you are right!")
   score+=3
else:
   print("sorry try again :( ")

ques4=input("what is your hobby? ")
if ques4.lower()=="drawing":
   print("you are right!")
   score+=4
else:
   print("sorry try again :( ")

ques5=input("what is your father name? ")
if ques5.lower()=="yam":
   print("you are right!")
   score+=5
else:
   print("sorry try again :( ")  

print("you got" + str(score)+ " question correct :) ")
