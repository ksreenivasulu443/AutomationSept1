class Student:
    def __init__(self):
        self.name = 'Sreeni'
        self.batch='001'
        print("this is __init__ method/ Constructor")
        """This is Student class"""
        print("this is inside cons")
    def display(self):
        #a=10
        print("Name is ",self.name)
        print("Batch is", self.batch)
        #print("the a value is",a)
        return self.batch

#Student().display()
s1 = Student() # S1 is the reference
            # variable using ref varibale we can access class related methods/variables

#print("This is batch",s1.batch)
#print("this is name",s1.name)
print(s1.display())
#s1.__init__()
#s1.display2()