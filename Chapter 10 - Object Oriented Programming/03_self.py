#Self is an convention

class Employee:
    name="John Doe"
    age="20"
    language="English"
    
    #Self is important without it we wont be able to use our variables in the methods
    def getInfo(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Language: {self.language}")
        
    def greet(self, na:str):
        print(f"Hello, I am {na} and I am looking for an employee named {self.name}")
        
    
emp1 = Employee()
emp2 = Employee()

emp1.getInfo()
emp1.greet("Ahmed")
