# Python Iterators
iter_list = iter(["apple", "banana", "cherry"])
print(next(iter_list))
print(next(iter_list))

# Python Generators
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for i in countdown(5):
    print(i)

# Python Scope
def outer_func():
    x = "local"
    def inner_func():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner_func()
    print("outer:", x)

outer_func()

# Python Modules - example with math module
import math
print(math.sqrt(16))

# Python Dates
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Python Math
import math
print(math.pow(2, 3))  # 2^3

# Python JSON
import json
json_data = '{"name": "John", "age": 30}'
python_obj = json.loads(json_data)
print(python_obj["name"])

# Using Regex to search and match string patterns in text
import re
text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
print(x)

# Metacharacters
pattern = r"ai"
match = re.findall(pattern, text)
print(match)

# Special Sequences
pattern = r"\bS\w+"
match = re.findall(pattern, text)
print(match)

# compile function
pattern = re.compile(r'\bS\w+')
match = pattern.findall(text)
print(match)

# Python File Handling - Read Files
with open("example.txt", "r") as file:
    print(file.read())

# Python Write/Create Files
with open("newfile.txt", "w") as file:
    file.write("Hello, World!")

# Python Delete Files
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")

# Working with directories
if not os.path.exists("myfolder"):
    os.makedirs("myfolder")

# Building function in Python
def greet(name):
    return "Hello, " + name

print(greet("John"))
