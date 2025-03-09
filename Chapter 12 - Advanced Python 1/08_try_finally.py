try:
    a = int(input("Enter a Number: "))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
finally: #Finally will run definately instead of anything..It will run
    print("Hey I am inside of Finally..!")
    
print("Thank YOU..!")


    