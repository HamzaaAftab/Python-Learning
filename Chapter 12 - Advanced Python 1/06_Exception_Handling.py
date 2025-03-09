try:
    a = int(input("Enter a Number: "))
    
except ValueError as v:
    print("Invalid input:", str(v))
except Exception as e:
    print("An error occurred:", str(e))
    
    
print("Thank YOU..!")    
        