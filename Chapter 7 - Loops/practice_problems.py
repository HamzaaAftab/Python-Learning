###Q.1: Write a program to print the Table of Given Number

n = int(input("Enter a Number: "))
mu = int(input("Enter the Number of Iterations you want: "))

for i in range(1,mu):
    print(f" {n} * {i} = ", n*i)
    

###Q.2: Write a program to greet the names in the list starts with S and H

li = ['Hamza', 'Shumaila', 'Harry', 'John', "Virat Kohli"]

for i in li:
    if(i.startswith("H") or i.startswith("S")):
        print(f'Hello {i}')

###Q.3: Write a program to print Q.1 from While Loop
# n = int(input("Enter a Number: "))
# mu = int(input("Enter the Number of Iterations you want: "))

i = 1
while i<=mu:
    print(f"{n} * {i} = {n*i}")
    i=i+1

###Q.4: Write a program to find whether the given program is prime or not

n = int(input("Enter a Number: "))
for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not a Prime Number")
        break
else:
    print(f"{n} is a Prime Number")
    
    
###Q.5: Write a program to find sum of numbers
n = int(input("Enter a Number: "))
i = 0
sum = 0
while (i<n):
    sum = sum + i
    i = i + 1

print(sum)