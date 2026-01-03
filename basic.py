#string
what="meghan adhikari"
print(what)

print(what +"is a beauty")

print(what.upper().isupper())

print(len(what))
print(what[0])
print(what.index("g"))
print(what.replace("meghan","mona"))

#numbers
print(2*3+5)
print(2*(3+5))

#changes the num into string
my_num=4
print(str(my_num))
#absolute value
my_num=-3
print(abs(my_num))
print(pow(3,5))
print(max(7,8))
print(min(8,9))
print(round(3.9))

from math import *
#floor takes the lowest num
print(floor(3.7))
#round up the num upwards even if its .lowest
print(ceil(3.2))
print(sqrt(9))

#input from users
name=input("enter your name : ")
age=input("enter your age : ")
print("hello" + name + " you are " + age )