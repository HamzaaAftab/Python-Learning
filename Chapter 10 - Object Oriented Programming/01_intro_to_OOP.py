### What is Class:
# Class is a blueprint to create objects...

##What are Objects?
# Objects are the instances of class..

# Classes specify which types of objects will be created and there..

# for suppose, there is a class called Fruits, it lies a blueprint for the objects, now what might be the objects for Fruits class? They are Apple, Mango and other fruits etc..

#Creating Class
class Employee:
    name = 'Hamza'
    language = 'Python'
    salary = 1200000
    
    def change_language(self, new_language):
        self.language = new_language
        def change_salary(self, new_salary):        
            self.salary = new_salary
    
# Creating Object

emp = Employee() # emp is now a object of clas Employee
emp.name = "Ahmed Salar"
print(f"Employee Created with the name {emp.name}. He is becoming expert in {emp.language} and getting a salary of {emp.salary} per month ")

# Class is a Noun..
# Objects are Adjective..
# Methods are Verbs...

emp2 = Employee() # emp is now a object of clas Employee
emp2.name = "John Doe"
emp2.language = "English"
emp2.salary = 12000000000000

print(f"Employee 2 Created with the name {emp2.name}. He is becoming expert in {emp2.language} and getting a salary of {emp2.salary} per month ")

# emp2 is object attribute and emp 1 attributes are of of the class attribute as they belong directly to the class,

