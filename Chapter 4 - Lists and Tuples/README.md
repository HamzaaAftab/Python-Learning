# 🐍 Python Lists & Tuples - A Comprehensive Guide

Welcome to the **Python Lists & Tuples** repository! 🚀 This guide covers everything about lists and tuples in Python, from basics to advanced manipulations. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to Lists & Tuples](#-introduction-to-lists--tuples)
🔹 [Creating Lists & Tuples](#-creating-lists--tuples)
🔹 [Accessing Elements](#-accessing-elements)
🔹 [List & Tuple Methods](#-list--tuple-methods)
🔹 [Modifying Lists](#-modifying-lists)
🔹 [Tuple Immutability](#-tuple-immutability)
🔹 [List vs. Tuple Comparison](#-list-vs-tuple-comparison)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to Lists & Tuples
Lists and tuples are built-in Python data structures that store multiple values.
- **Lists** are mutable (can be modified).
- **Tuples** are immutable (cannot be changed after creation).

```python
my_list = [1, 2, 3, "hello"]
my_tuple = (1, 2, 3, "hello")
```

---

## ✏️ Creating Lists & Tuples
### 🔹 Creating a List
```python
fruits = ["apple", "banana", "cherry"]
```

### 🔹 Creating a Tuple
```python
days = ("Monday", "Tuesday", "Wednesday")
```

---

## 🔍 Accessing Elements
Both lists and tuples allow indexing:

```python
print(fruits[0])  # apple
print(days[-1])   # Wednesday
```

---

## 🛠️ List & Tuple Methods
### 🔹 Common List Methods
```python
fruits.append("orange")  # Adds an element
fruits.remove("banana")  # Removes an element
fruits.sort()            # Sorts the list
print(len(fruits))       # Length of list
```

### 🔹 Common Tuple Methods
Tuples have limited methods since they are immutable:
```python
print(days.count("Monday"))  # Counts occurrences
print(days.index("Tuesday")) # Finds index
```

---

## 🔄 Modifying Lists
Lists are mutable, allowing modifications:
```python
fruits[0] = "grape"
fruits.append("kiwi")
print(fruits)
```

---

## 🔒 Tuple Immutability
Tuples cannot be modified:
```python
days[0] = "Sunday"  # TypeError
```

---

## ⚖️ List vs. Tuple Comparison
| Feature      | List  | Tuple  |
|-------------|-------|--------|
| Mutability  | ✅ Yes | ❌ No  |
| Performance | ⬇ Slower | ⬆ Faster |
| Methods     | ✅ Many | ❌ Few |

---

## 🎯 Conclusion
Lists and tuples are essential in Python for storing collections of data. Understanding when to use each is key to writing efficient Python code. Happy coding! 🚀🔥

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐