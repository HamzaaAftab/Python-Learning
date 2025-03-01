f = open('myFile.txt')

# Read the file line by line
lines = f.readlines()
print(lines)
print(type(lines))
f.close() # Close

# Read the file line by line using a loop
f = open('myFile.txt')
for line in lines:
    print(line.strip())

f.close() # Close