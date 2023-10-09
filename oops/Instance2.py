class Test:
    def __init__(self):
        self.name='Sreeni'
    def add(self):
        self.rollno=101

obj = Test()
obj.add()

obj2 = Test()

print(obj.__dict__)
print(obj2.__dict__)
obj2.add()
print(obj2.__dict__)

obj2.d=40

print(obj2.__dict__)