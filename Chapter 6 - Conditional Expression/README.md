# 🐍 Python Conditional Expressions - A Comprehensive Guide

Welcome to the **Python Conditional Expressions** repository! 🚀 This guide covers everything about conditional expressions in Python, from basics to advanced usage. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to Conditional Expressions](#-introduction-to-conditional-expressions)
🔹 [if Statement](#-if-statement)
🔹 [if-else Statement](#-if-else-statement)
🔹 [if-elif-else Statement](#-if-elif-else-statement)
🔹 [Ternary Conditional Expressions](#-ternary-conditional-expressions)
🔹 [Nested Conditional Expressions](#-nested-conditional-expressions)
🔹 [Best Practices](#-best-practices)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to Conditional Expressions
Conditional expressions allow you to control the flow of a Python program based on conditions. These expressions evaluate to either **True** or **False** and help execute different code blocks accordingly.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## ✏️ if Statement
The `if` statement executes a block of code if the condition is **True**:
```python
age = 18
if age >= 18:
    print("You are eligible to vote!")
```

---

## 🔄 if-else Statement
The `if-else` statement executes one block if the condition is **True** and another if it is **False**:
```python
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## 🔍 if-elif-else Statement
Use `if-elif-else` when multiple conditions need to be checked:
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

---

## ⚡ Ternary Conditional Expressions
A shorthand way to write `if-else` statements:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

---

## 🔄 Nested Conditional Expressions
Conditional expressions can be nested for complex logic:
```python
num = 5
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")
```

---

## 🏆 Best Practices
✔️ Keep conditions simple and readable.  
✔️ Avoid deep nesting; use logical operators (`and`, `or`).  
✔️ Use ternary expressions for concise conditions.  
✔️ Prefer `elif` over multiple `if` statements.  

---

## 🎯 Conclusion
Conditional expressions are essential in Python programming. Understanding them improves your ability to write efficient and logical code. Happy coding! 🚀🔥

---

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐