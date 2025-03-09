a = int(input("Enter a Number One: "))
b = int(input("Enter a Number Second: "))

if(b==0):
    raise ZeroDivisionError("Number two must not be zero")
else:
    print(f"The Sum is {a + b}")

