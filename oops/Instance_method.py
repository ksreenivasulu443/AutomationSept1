class Student:
    college_name='CREC' # Class variable/Static variable
    director_name='XYZ'
    branch='ECE'
    def __init__(self,rollno, name):
        print(self.director_name)
        self.rollno=rollno # Instance variable
        self.name=name # Instance variable
        print("Inside con",Student.director_name)
        self.z=19
        Student.branch_hod_name = 'ABC'
    def display(self): # If we use atleast one instance variable then we call it as instance method
        print("Student rollno is", self.rollno)
        print("student name is", self.name)
        print("The college name is", Student.college_name)
        self.e = 50
        self.z = 20
        Student.classroom_no=9001
    @classmethod
    def college_info(cls): # If we are not using any instance variable and using only class variables then we call it as Class method
        print("College name is ", cls.college_name)
        print("The director name", cls.director_name)
        cls.new_variable=3404
        Student.new_variable2 ='New_var'
        #print("student roll", cls.rollno)
    @classmethod
    def branch_info(cls):
        print("Branch name is", cls.branch)
    @staticmethod
    def add():
        a=10
        b=20
        Student.new_variabl3 = "new_variable3"
        Student.college_name
        print("Sum of two number", a+b)


obj = Student(101,'Sreeni')

print(obj.__dict__)

obj.display()
obj.college_info()
obj.add()
print(obj.__dict__)
obj.z=200
print(obj.__dict__)

del obj.z

print(obj.__dict__)
print(Student.__dict__)
obj.college_name
# obj1 = Student(102,'Mahesh')
# obj1 = Student(103,'Chandan')

# obj.display()
# obj.college_info()
# obj.branch_info()
# obj.add()
#
# obj2 = Student(102,'Raghav')
#
# obj3 = Student(103,'Deep')
#
#
#print(Student.__dict__)
# print(obj.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
#
# obj3.e=5000
# obj3.f=15000
# print(obj3.__dict__)
#
#
# print(obj2.name)
# print(obj2.rollno)
