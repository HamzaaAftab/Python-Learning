# a = input('Enter Number 1: ')
# b = input('Enter Number 2: ')

# print(' Number a is:', a)
# print(' Number a is: ', b)
# print(' Addition of Both numbers are: ', a+b)

#The Key point in the above program is whenever you input a number, you might be thinking of it as a number but behind the python, it takes input as a string by default, therefore we need to specify that it is number by type casting, here's how:


c = int(input('Number a is:'))
d = int(input('Number b is:'))
e = int(c+d)
print('Addition of both numbers are:', int(e) )