
class Student ():
    def __init__(self,name,age,gender,subjects,marks):
        self.name=name
        self.age=age
        self.gender=gender
        self.subjects=subjects
        self.marks=marks
    def mark(self):
        print("u have scored:-")
    def subject(self):
        print("ur subjects are :-")

rohan = Student("rohan",15,"male","5",50/100)

print(rohan.mark())