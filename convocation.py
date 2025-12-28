class user():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def show_details(self):
        print(f"hi i am {self.first_name} {self.last_name}")

class student(user):
    def __init__(self, first_name, last_name,year,division):
     user.__init__(self,first_name, last_name)
     self.first_name=first_name
     self.last_name=last_name
     self.year=year
     self.division=division

     def congrats_msg(user):
        print(f"congrats {self.first_name} {self.last_name}\n you have passed on the year {self.year}\n with {self.division}division")

object2=student("meghan","adhikari",2082,1)
print (object2.first_name)
print(object2.last_name)
print(object2.year)
print(object2.division)