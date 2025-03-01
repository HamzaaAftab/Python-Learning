# 📂 Python File I/O - A Comprehensive Guide

Welcome to the **Python File I/O** repository! 🚀 This guide covers everything about reading, writing, and handling files in Python. Whether you're a beginner or an experienced developer, you'll find valuable insights here. 🎯

---

## 📌 Table of Contents
🔹 [Introduction to File Handling](#-introduction-to-file-handling)
🔹 [Opening a File](#-opening-a-file)
🔹 [Reading a File](#-reading-a-file)
🔹 [Writing to a File](#-writing-to-a-file)
🔹 [Appending to a File](#-appending-to-a-file)
🔹 [File Handling Using `with` Statement](#-file-handling-using-with-statement)
🔹 [Working with Different File Modes](#-working-with-different-file-modes)
🔹 [Handling File Exceptions](#-handling-file-exceptions)
🔹 [Best Practices](#-best-practices)
🔹 [Conclusion](#-conclusion)

---

## 📜 Introduction to File Handling
File I/O (Input/Output) in Python allows reading and writing data to files. Python provides built-in functions to interact with files efficiently.

```python
# Opening a file
file = open("example.txt", "r")
content = file.read()
file.close()
```

---

## 📂 Opening a File
Files in Python can be opened using the `open()` function:
```python
file = open("sample.txt", "r")
```

Modes of opening files:
- **`r`** - Read (default)
- **`w`** - Write (creates file if not exists)
- **`a`** - Append
- **`rb`/`wb`** - Read/Write in binary mode

---

## 📖 Reading a File
```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

### 🔹 Reading Line by Line
```python
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

---

## ✍️ Writing to a File
```python
file = open("output.txt", "w")
file.write("Hello, Python File I/O!")
file.close()
```

⚠️ **Warning:** The `w` mode overwrites existing content.

---

## ➕ Appending to a File
```python
file = open("output.txt", "a")
file.write("\nAppending new content.")
file.close()
```

---

## ✅ File Handling Using `with` Statement
Using `with` ensures automatic file closure, preventing memory leaks.
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 🔄 Working with Different File Modes
```python
# Writing in binary mode
with open("image.jpg", "rb") as file:
    data = file.read()
```

```python
# Writing JSON data to a file
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)
```

---

## ⚠️ Handling File Exceptions
Always handle exceptions to avoid runtime errors:
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

---

## 🏆 Best Practices
✔️ Always close files after use (or use `with`).  
✔️ Handle exceptions to prevent crashes.  
✔️ Use appropriate file modes (`r`, `w`, `a`).  
✔️ Avoid using `w` mode if you don’t want to overwrite existing data.  

---

## 🎯 Conclusion
File I/O is essential for handling data in Python applications. Mastering it will help you work with files efficiently. Happy coding! 🚀🔥

---

---

📌 **Author:** Hamza Aftab  
📌 **GitHub Repository:** https://github.com/HamzaaAftab/Python-Learning
📌 **License:** MIT  

⭐ **If you found this helpful, don't forget to star the repository!** ⭐