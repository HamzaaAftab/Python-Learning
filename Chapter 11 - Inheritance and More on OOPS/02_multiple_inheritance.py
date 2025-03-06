class Employee:
    name="John Smith"
    language="Python"
    
    def show(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        
class Coder:
    languages=["Python", "Java", "C++", "Javascript"]
    
class Test(Employee, Coder): # Multiple Inheritance
    def show(self):
        print("I can use both the Properties of Employee and Coder Classes")
        
t = Test() # Test class can now use all the attributes and properties of Employee and Coder Classe.
print(t.name, "\t", t.language, "\t", t.languages, "\n",)
print(t.show)
    
    