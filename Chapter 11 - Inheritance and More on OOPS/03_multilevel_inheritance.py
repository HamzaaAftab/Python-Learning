class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

# Employee cannot access b, because Employee has no idea about B but programmer can use A.
# Manager can use both A and B because of th hierarchical structure..
m = Manager()
print(m.a)