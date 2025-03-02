# constructor 
# In pytho, __ methods are called as Dunder methods which is automatically called...
# _init_is one of the those, even if you dont call it it will run..
# Upon making an object, the _init_ method will automatically be called


class Employee:
    name="John Doe"
    age="20"
    language="English"
    
    #Constructor
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print(f"Employee {self.name} with the salary {self.salary} and expertize in language {language} created")
    
    #Self is important without it we wont be able to use our variables in the methods
    def getInfo(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Language: {self.language}")
        
    def greet(self, na:str):
        print(f"Hello, I am {na} and I am looking for an employee named {self.name}")
        
    
emp1 = Employee("Rameez", 240000, "Python") # Object of Employee
emp2 = Employee("John Doe", 240000, "Python") # 2nd Object of Employee

emp1.getInfo()
emp1.greet("Ahmed")
