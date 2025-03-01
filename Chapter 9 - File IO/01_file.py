# what is file
# file is a variable that holds the path to a file
# we can use the file variable to open the file in read mode
# we can use the file variable to write to the file
# we can use the file variable to read from the file
# we can use the file variable to close the file

f = open('file.txt')
data = f.read()

# print the data
print(data)
f.close()

# Remember whenever you open a file it is ncessary for you to close the file just like above f.close()
# or you can use with keyword which automatically closes the file when you are done with it

with open('file.txt') as f:
    data = f.read()
    
print(data)

#OPEN Function takes two arguments, a file path and a mod, mod refers to read and write etc. Default mod is Read..

