# Sometimes we need to thing in a repetition, means if we have to print something 100 times, What will we do? We cannot use print statement for 100 times, this is not efficient way. So in programming we use loops in order to acheive tasks that are repetitive..

# for loop
print('For Looop \n' )
for i in range(1,9): # Will print till 8 because it starts from 0
    print(i)
    
#while loop
i = 1

print(' \n While Loop \n' )
while i <= 8:
    print(i)
    i += 1 # incrementing the value of i by 1 after each iteration to keep the loop going.
    
# Diff between while and for:
    # For loop: It is used when we know the exact number of times we want to repeat a task.
    # While loop: It is used when we don't know the exact number of times we want to repeat a task.

#Quick Quiz: Write a while loop to print 1 to 5

# i=1

# while i <=50:
#     print(i)
#     i += 1
