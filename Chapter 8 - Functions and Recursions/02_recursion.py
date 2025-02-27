# Recursion is a function which call itself..
# Perfect example of recursion is factorial...
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))