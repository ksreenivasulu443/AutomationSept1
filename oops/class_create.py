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