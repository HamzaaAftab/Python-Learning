# to check type of any variabe, we simply use type() function

a = 10
b = 'hello'
c = [1, 2, 3]
d= 31.2
e = True

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'str'>
print(type(c))  # Output: <class 'list'> # List refers to Arrays
print(type(d)) # Output: <class 'float'>
print(type(e)) # Output: <class 'bool'>

###TYPE CASTING -> Means to convert a Type to a different type if it is valid, valid means you cannot convert 'Hamza' or "Harry" to a Number of Float Type.

a = str(a)
print(type(a))
