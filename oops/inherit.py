class Parent:
    def property(self):
        print("this is property class")
    def marry(self):
        print("Parent marry method")

class child(Parent):
    def marry(self):
        print("child marry method")

obj_c = child()

obj_c.marry()
obj_c.property()