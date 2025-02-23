#Q.1: Store input 7 names in the list

fruits = []
f1 = input('Enter a Fruit Name: ')
fruits.append(f1)
f2 = input('Enter a Fruit Name: ')
fruits.append(f2)

# print(fruits)

#and goes on till f7

##Q.2: Accept 6 inputs and show them in sort order

num_list = []
for i in range(6):
    num = int(input('Enter a Number: ' ))
    num_list.append(num)
num_list.sort()
print(num_list)
    

##Q.3: Check that tuple type cannot be changed in python

tuple = (34, 54)

tuple[0] = 50 #this will throw error


##Q.4: Sum a list with 4 numbers

list = [1, 2, 3, 4]

print(sum(list))

##Q.5: Write a program to find the maximum and minimum values in a list

list = [2, 4, 6, 8, 10]

max_value = max(list)
min_value = min(list)

print('Maximum Value:', max_value)

print('Minimum Value:', min_value)

###Q.6: Write a program to count the number of specified number in a tuple

tuple = (2, 4, 6, 8, 2, 4, 6)
num = 2

count = tuple.count(num)
print(count)