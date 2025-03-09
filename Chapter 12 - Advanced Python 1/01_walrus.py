# Walrus Operator Allows you to assign values to variables as part of an expression. 

if(n := len([1,3,4,5,6])) > 3:
    print(f"The List is too long ({n} elements, expected <=3)")