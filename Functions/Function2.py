class Person:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def myfunc(self):
    print(f"Hello my name {self.a} is " + str(self.b))
    print(self.a+self.b)

p1 = Person(40, 36)
p1.myfunc()