class Employee:
    def __init__(self, name, age, salary, sex):
        self.name=name
        self.age=age
        self.salary=salary
        self.sex=sex
    def sal(self):
        print("This is inside sal",self.salary)

obj = Employee('sreeni',28,3000,"M")

obj.sal()