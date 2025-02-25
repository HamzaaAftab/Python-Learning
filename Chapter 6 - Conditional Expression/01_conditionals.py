#IF, ELIF and ELSE are conditional statements, if you want to make decisions about whether you want to make decisions about a particular condition..
# IF the day is rainy, we will drink coffee or tea otherwise not.
# whenever we want to specify decision making, we will use Conditional statements..
#IF, ELIF and ELSE Ladder:

a = int(input('Enter your Age: '))

if(a>0 and a<=18):
    print('You are an Adult')
    print("Good For you Boy")
elif(a>40):
    print('You are a Senior Citizen')
elif(a<0):
    print('Enter a +ve Age')
else:
    print('You are a Child')

print("End of Program")    