# 🐍 Python Dictionary & Sets - A Comprehensive Guide

Welcome to the **Python Dictionary & Sets** repository! 🚀 This guide covers everything about dictionaries and sets in Python, from basics to advanced usage. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to Dictionary & Sets](#-introduction-to-dictionary--sets)
🔹 [Creating a Dictionary](#-creating-a-dictionary)
🔹 [Dictionary Methods](#-dictionary-methods)
🔹 [Creating a Set](#-creating-a-set)
🔹 [Set Operations](#-set-operations)
🔹 [Dictionary vs. Set Comparison](#-dictionary-vs-set-comparison)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to Dictionary & Sets
- **Dictionaries** store key-value pairs and allow fast lookups.
- **Sets** store unique elements and are useful for membership tests and mathematical operations.

```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_set = {1, 2, 3, 4, 5}
```

---

## ✏️ Creating a Dictionary
Dictionaries use curly braces `{}` with key-value pairs:
```python
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
print(student["name"])  # Output: John
```

---

## 🛠️ Dictionary Methods
### 🔹 Common Dictionary Methods
```python
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.keys())    # Get all keys
print(dict1.values())  # Get all values
print(dict1.items())   # Get all key-value pairs
dict1.update({"d": 4}) # Add a new key-value pair
print(dict1.get("b"))  # Get value for key 'b'
```

---

## ✏️ Creating a Set
Sets are created using curly braces `{}` or the `set()` function:
```python
numbers = {1, 2, 3, 4, 5}
names = set(["Alice", "Bob", "Charlie"])
```

---

## 🔄 Set Operations
### 🔹 Common Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 5, 6}
```

---

## ⚖️ Dictionary vs. Set Comparison
| Feature      | Dictionary | Set |
|-------------|------------|------|
| Storage     | Key-Value Pairs | Unique Elements |
| Order       | ✅ Preserved (Python 3.7+) | ❌ Unordered |
| Mutability  | ✅ Mutable | ✅ Mutable |
| Lookup Time | ⏩ Fast (O(1)) | ⏩ Fast (O(1)) |

---

## 🎯 Conclusion
Dictionaries and sets are powerful Python data structures that enhance data storage and manipulation. Mastering them will significantly improve your coding efficiency. Happy coding! 🚀🔥

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐