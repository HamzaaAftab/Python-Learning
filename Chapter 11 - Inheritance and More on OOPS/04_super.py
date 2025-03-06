# Super Keyword in OOP

class Employee:
    a=1
    def __init__(self):
        print("Employee constructor")

class Programmer(Employee):
    b=2
    def __init__(self):
        print("Programmer constructor")
        super().__init__() # Super makes sure the parent constructor also runs or other functions

class Manager(Programmer):
    c=3

b = Programmer()

# Using Super you can use the methods and everything of the Parent Class.
