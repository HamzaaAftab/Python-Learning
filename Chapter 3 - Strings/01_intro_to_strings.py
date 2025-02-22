# Strings can be represented as '', "", and triple quotes ''', ''''.
# String is a data type in a python
# String is a sequence of characters.

# String Slicing
# Remember string is immutable, means if it is created it cannot be changed or modified. 

####################STRING IS MUTABLE

name = 'Hamza'

#Index, remember at 0 position lies the first character of the string..
# In reverse it is started as -1.

short = name[0:3]

print(len(name)) # to find the length of the string

# In order to slice string, [0:3], 0 means starting from index 0 and 3 is ending point, means it wil start from 0th index upto till 3rd index. Remember the last index will not be included.

print(short) # to find the length of the string

character1 = name[1]
print(character1)

##NEGATIVE SLICING
neg = 'python'
    
negCharacters = neg[-4:-1]
posCharacters = neg[1:4]

## I suggest you to convert the negative into positive by corresponding numbers, means if you are ask to slice the negative string from -4 index to -1 index, you can simply convert the negative into positive and change the orders, meanings 1st index to 4th index respectively..

print(negCharacters)
print(posCharacters)

print(f'\nNot Mentioning the Indexes')
print(neg[:4]) # this will print from 0th index to 4th because we didn't specify the starting index so it will print from 0th or starting index till the index we specified.

print(neg[4:]) # this will print from 4th index to the end because we didn't specify the ending index so it will print till the end of the string..


word = 'amamaaadgsdgjlsdgkljsadgasdglkjasdgajsldzinggggggg'
skippedWord = word[1:2:2]
print(skippedWord)





