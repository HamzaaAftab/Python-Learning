marks = int(input("Enter your Marks to check out your Result: "))

if(marks>=90):
    print("Grade: A")
    print("Congratulations! You have Passed with an A grade.")
elif(marks<90 and marks>70):
    print("Grade: B")
    print("Congratulations! You have Passed with a B grade.")
elif(marks<70 and marks>50):
    print("Grade: C")
    print("Congratulations! You have Passed with a C grade.")
elif(marks<50 and marks>30):
    print("Grade: D")
    print("Congratulations! You have Passed with a D grade.")
elif(marks<0):
    print("Enter a Positive Marks...!")
else:
    print("Grade: F")
    print("Sorry! You have Failed with an F grade.")

print("End of Program")