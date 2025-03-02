# Static methods are those who dont need self, means no need of object

class Employee:
    name="John Doe"
    age="20"
    language="English"
    
    #Self is important without it we wont be able to use our variables in the methods
    def getInfo(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Language: {self.language}")
        
        #Static Method
    @staticmethod
    def greet():
        print("Hello, welcome to our company!")

    
emp1 = Employee()
emp2 = Employee()

emp1.getInfo()
emp1.greet()
