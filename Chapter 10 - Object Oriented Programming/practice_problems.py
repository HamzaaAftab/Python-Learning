###### Q.1: Create a class programmer and store information about programmers working for micrsoft

class Programmer:
    company = "Microsft Inc" # Class Attribute
    def __init__(self, name, salary, pincode):
        self.name = name # Instance Attribute
        self.salary = salary # Instance Attribute
        self.pincode = pincode # Instance Attribute
        
    def getInfo(self):
        print(f"The name of the Programmer is {self.name}")
        print(f"The salary of the Programmer is {self.salary}")
        print(f"The pincode of the Programmer is {self.pincode}")
        print(f"The company of the Programmer is {self.company}")
        
# Creating object of the class
p1 = Programmer("Hamza", 1500000, 123456)
p1.getInfo()

p1 = Programmer("Moeed", 1500000, 1563456)
p1.getInfo()



####Q.2: Calculator Class to calculate some methods

class Calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The Number Entered is {self.n} and the Square is {self.n * self.n}")
        
    def cube(self):
        print(f"The Number Entered is {self.n} and the Cube is {self.n * self.n *self.n}")
        
c1 = Calculator(12)
c1.square()
c1.cube()

####Q.3: Its about Class Attributes and Object Attributes which we done earlier, let's do it again

class Employee:
    name = "John Doe" # Class Attribute
    
    def __init__(self):
        pass
        
# Creating object of the class
e1 = Employee()
# Now the task is we need to check if Instance Attribute replaces the class Attribute, It will surely yes because the instance has preference over class attributes
e1.name="Hamza Aftab"
print(e1.name) # Now it will print Hamza Aftab instead of John Doe