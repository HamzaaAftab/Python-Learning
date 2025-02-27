# 🔄 Python Functions & Recursion - A Comprehensive Guide

Welcome to the **Python Functions & Recursion** repository! 🚀 This guide covers everything about functions and recursion in Python, from basics to advanced usage. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to Functions](#-introduction-to-functions)
🔹 [Defining a Function](#-defining-a-function)
🔹 [Function Parameters & Arguments](#-function-parameters--arguments)
🔹 [Return Statement](#-return-statement)
🔹 [Lambda Functions](#-lambda-functions)
🔹 [Recursion in Python](#-recursion-in-python)
🔹 [Best Practices](#-best-practices)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to Functions
Functions in Python allow code reuse, improve readability, and make programs modular. A function is a block of reusable code that performs a specific task.

```python
def greet():
    print("Hello, World!")
```

---

## 🛠️ Defining a Function
Functions are defined using the `def` keyword:
```python
def add(a, b):
    return a + b
```

---

## 🔹 Function Parameters & Arguments
Functions can take multiple arguments:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### 🔹 Default Arguments
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
```

### 🔹 Keyword Arguments
```python
def introduce(name, age):
    print(f"Name: {name}, Age: {age}")

introduce(age=25, name="Bob")
```

---

## 🔄 Return Statement
The `return` statement is used to return a value from a function:
```python
def square(num):
    return num * num

result = square(4)
print(result)  # Output: 16
```

---

## ⚡ Lambda Functions
Lambda functions are anonymous, one-liner functions:
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## 🔄 Recursion in Python
Recursion is a function calling itself to solve problems that can be broken down into smaller instances.

### 🔹 Example: Factorial Using Recursion
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### 🔹 Example: Fibonacci Using Recursion
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```

---

## 🏆 Best Practices
✔️ Use meaningful function names.  
✔️ Keep functions short and focused on a single task.  
✔️ Use default and keyword arguments for flexibility.  
✔️ Avoid deep recursion to prevent stack overflow errors.  
✔️ Use memoization techniques to optimize recursive functions.  

---

## 🎯 Conclusion
Functions and recursion are essential concepts in Python. Mastering them will make your code more efficient, modular, and readable. Happy coding! 🚀🔥

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐