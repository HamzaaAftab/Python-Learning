# 🔁 Python Loops - A Comprehensive Guide

Welcome to the **Python Loops** repository! 🚀 This guide covers everything about loops in Python, from basics to advanced usage. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to Loops](#-introduction-to-loops)
🔹 [for Loop](#-for-loop)
🔹 [while Loop](#-while-loop)
🔹 [Loop Control Statements](#-loop-control-statements)
🔹 [Nested Loops](#-nested-loops)
🔹 [List Comprehensions with Loops](#-list-comprehensions-with-loops)
🔹 [Best Practices](#-best-practices)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to Loops
Loops in Python allow you to execute a block of code multiple times. They are useful when iterating over sequences like lists, tuples, and strings.

```python
for i in range(5):
    print("Iteration", i)
```

---

## 🔄 for Loop
The `for` loop is used to iterate over a sequence (list, tuple, dictionary, set, or string):
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 🔄 while Loop
The `while` loop executes as long as a condition is **True**:
```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

---

## ⏭️ Loop Control Statements
Loop control statements alter the normal loop execution:

### 🔹 break Statement
Used to exit a loop immediately:
```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

### 🔹 continue Statement
Skips the current iteration and moves to the next one:
```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```

### 🔹 pass Statement
Used as a placeholder where code is needed but not yet written:
```python
for _ in range(5):
    pass  # Placeholder for future code
```

---

## 🔄 Nested Loops
Loops inside loops allow iterating over multiple dimensions:
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

---

## 🚀 List Comprehensions with Loops
A concise way to create lists using loops:
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## 🏆 Best Practices
✔️ Use `for` loops when iterating over sequences.  
✔️ Use `while` loops only when necessary to avoid infinite loops.  
✔️ Use `break` and `continue` wisely to maintain readability.  
✔️ Prefer list comprehensions for concise, readable code.  

---

## 🎯 Conclusion
Loops are fundamental in Python programming and help automate repetitive tasks. Mastering them will significantly improve your coding efficiency. Happy coding! 🚀🔥

---

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐