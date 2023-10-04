class Test:
    def __init__(self):
        a.name='Sreeni'
        print("One arg constructor")
        print("The id of a is ", id(self))
    # def __init__(self,a):
    #     print("two arg constructor")
    # def __init__(self):
    #     print("One arg constructor")
    #     print("hjsagdhsfd")
    def display(self):
        print("this is Test method")
        print(self.name)

obj = Test() # Here obj is reference varible to Test() object
print("The id of obj object is ", id(obj))



