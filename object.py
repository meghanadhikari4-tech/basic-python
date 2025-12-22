class student:
    def __init__(self,name,grade):
     self.name=name
     self.grade=grade
     
     def student_details(self):
        print(f'{self.name} is in class {self.grade}')
student1=student ('meghan',11)
print(student1.name,student1.grade)
student2=student('ram',12)
print(student2.name,student2.grade)
