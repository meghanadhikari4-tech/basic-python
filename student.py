class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("grade:",self.marks)
    def grade(self):
        if self.marks>=90:
            return"A"
        elif self.marks>=60:
            return"B"
        elif self.marks>=35:
            return"C"
        else:
            return
s1=student("meghan",85)
s1.display()
print("grade:",s1.grade())

