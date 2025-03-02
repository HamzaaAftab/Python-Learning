class Employee:
    name = "Harry"  # This is the class attribute
    language = "py"

emp1= Employee()
emp2= Employee()

print(f"Employee 1 created with the name {emp1.name}. He is learning {emp1.language}")

emp2.language= "Javascript and React" # This is an instance attribute    
print(f"Employee 2 created with the name {emp2.name}. He is learning {emp2.language}")

#If there's an instance attribute it will print that, otherwise it will print class attributes..
# In short Instance Attributes taken preference over class attributes..