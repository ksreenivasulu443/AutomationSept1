class Student:
    college_name='CREC' # Class variable/Static variable
    director_name='XYZ'
    branch='ECE'
    def __init__(self,rollno, name):
        self.rollno=rollno # Instance variable
        self.name=name # Instance variable
        self.d=40
        print("Inside con",Student.director_name)
    def display(self): # If we use atleast one instance variable then we call it as instance method
        print("Student rollno is", self.rollno)
        print("student name is", self.name)
        print("The college name is", self.college_name)
    @classmethod
    def college_info(cls): # If we are not using any instance variable and using only class variables then we call it as Class method
        print("College name is ", cls.college_name)
        print("The student name", cls.director_name)
        #print("student roll", cls.rollno)
    @classmethod
    def branch_info(cls):
        print("Branch name is", cls.branch)
    @staticmethod
    def add():
        a=10
        b=20
        print("Sum of two number", a+b)









obj = Student(101,'Sreeni')
# obj1 = Student(102,'Mahesh')
# obj1 = Student(103,'Chandan')

obj.display()
obj.college_info()
obj.branch_info()
obj.add()

print(Student.__dict__)
print(obj.__dict__)
