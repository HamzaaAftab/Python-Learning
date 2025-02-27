### WHAT IF FUNCTION:
# Whenever we need to store a particular piece of program and want to use it back to back, we do that by using Functions. Functions are defined for a partcular task. Lets suppose if we want to add numbers and we have to use that in many areas in our program, we will simply create a function that adds numbers and use that program wherever we need, This way we wont have to write the code again and again, Just write it once and use it anywhere you want...


#Function Definition
def average():
    a = 12

    b= 45 

    c= 56

    print((a+b+c)/3)

#Function Call
average()

#Function Definition with Arguments
def average_with_arguments(x,y,z):
    print((x+y+z)/3)

#Function Call with Arguments
average_with_arguments(122, 4455, 4456)
average_with_arguments(1, 4455, 6)

# QUICK QUIZ
def greet(name):
    print("Hello, Good Day to you Sir !", name)
    
greet("Hamza")

#TYPES OF FUNCTIONS
# USER_DEFINED FUNCTIONS: THOSE FUNCTIONS THAT ARE CREATED BY USERS LIKE WE DID ABOVE..
# INBUILT FUNCTIONS: THOSE FUNCTIONS THAT ARE PROVIDED BY PYTHON OR ANY OTHER PROGRAMMING LANGUAGES, SUCH AS sort, startsWith, endsWith etc...
# print() is the most common example of Python provided inbuilt functions..

def goodDay(name, ending):
    print("Hello, Good Day to you Sir !", name)
    print(ending)

goodDay("Hamza", "See you later!")

# Now if we want to store it into variable, we need to use return statement

def goodDayWithReturn(name, ending):
    return "Hello, Good Day to you Sir !", name, ending

result = goodDayWithReturn("Hamza", "See you later!")
print(result)