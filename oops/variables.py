
class College:
    college = 'SVCE'
    Director_name = 'XYZ'
    def __init__(self, name, rollno, branch):
        self.name=name
        self.rollno=rollno
        self.branch=branch
    @staticmethod
    def add():
        a=10
        b=20
        add=a+b

s1 = College('Sreeni',1,'ECE')
s2 = College("Suraj",2,'MEC')
