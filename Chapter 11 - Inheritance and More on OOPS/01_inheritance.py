class Employee:
    def show(self):
        print(f"The Name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    # def show(self):
    #     print(f"The Name is {self.name} and the salary is {self.salary}, and the programming language is {self.language}")
        
    def showLanguages(self):
        print(f"The programmer can write in {self.languages}")
        
# Inheritance refers to inherit all the attributes and methods from thhe class.

a = Employee()
b = Programmer()
b.name = "John Smith"
b.salary = 23444
print(b.show())        

# Types of Inheritance: 1) Single Inheritance 2) Multiple Inheritance 