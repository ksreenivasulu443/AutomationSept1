#
# class College:
#     college = 'SVCE'
#     Director_name = 'XYZ'
#     def __init__(self, name, rollno, branch):
#         self.name=name
#         self.rollno=rollno
#         self.branch=branch
#         self.friend='Hari'
#     def display(self):
#         self.name2 = 'Kattu'
#         print(self.college)
#         del self.friend
#     @staticmethod
#     def add():
#         a=10
#         b=20
#         add=a+b
#
# s1 = College('Sreeni',1,'ECE')
# s2 = College("Suraj",2,'MEC')
# s1.display()
# s1.name3 = 'Rahul'
# print(s1.__dict__)
# print(College.__dict__)
# del s1.name3
# print(s1.__dict__)
#
# College.Director_name

class college:
    college_name='CREC'
    def __init__(self):
        self.name=('Sreeni')
    def display(self):
        college.hod='ABC'

#s1=college()
print(college.__dict__)