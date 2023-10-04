class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.b-self.a

obj = test(10,20)
sum1= obj.add()
sub1 = obj.sub()

print(sum1,sub1)

print(obj.a)

class test:
    def add(self,a,b):
        a=4
        return a+b
    def sub(a,b):
        return a-b

obj2 = test()
add1 = obj2.add(4,5)
print(add1)

