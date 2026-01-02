# Lesson 2: Understanding Variables

## Overview

Variables are fundamental building blocks in Python programming. They act as containers that store data values, allowing you to save information and use it throughout your program. Understanding variables is essential for writing effective Python code.

**Learning Objectives:**
- Understand what variables are and why they are important
- Learn how to create and name variables in Python
- Explore different data types stored in variables
- Practice variable assignment and reassignment

---

## Video Tutorial

Watch the video lesson for this topic:

https://www.youtube.com/embed/jE3A1LZom8w

**Direct Link:** [Watch on YouTube](https://youtu.be/jE3A1LZom8w)

---

## Key Concepts

### What is a Variable?

A **variable** is a named location in computer memory that stores a value. Think of it as a labeled box where you can put different types of information.

**Key Points:**
- Variables have a **name** (identifier) and a **value**
- Python is **dynamically typed**: you do not need to declare the type explicitly
- Variables can be reassigned to different values and types

### Variable Naming Rules

1. **Must start with**: A letter (a-z, A-Z) or underscore (_)
2. **Can contain**: Letters, numbers (0-9), and underscores
3. **Cannot contain**: Spaces or special characters (@, #, $, etc.)
4. **Case-sensitive**: `age` and `Age` are different variables
5. **Cannot use**: Python keywords (like `if`, `for`, `while`, etc.)

**Naming Conventions:**
- Use descriptive names: `student_age` instead of `sa`
- Use lowercase with underscores for multi-word names (snake_case): `first_name`
- Avoid starting with numbers: `2ndplace` is invalid

---

## Detailed Explanations

### Creating Variables

In Python, you create a variable by assigning a value using the assignment operator `=`.

**Syntax:**
```python
variable_name = value
```

### Common Data Types

Variables can store different types of data:

| Data Type | Description | Example |
|-----------|-------------|---------|
| **int** | Integer (whole number) | `age = 25` |
| **float** | Decimal number | `price = 19.99` |
| **str** | String (text) | `name = "Alice"` |
| **bool** | Boolean (True/False) | `is_active = True` |

### Variable Reassignment

You can change the value of a variable at any time:

```python
x = 10      # x is an integer
x = "Hello" # x is now a string
```

---

## Important Points to Remember

- **No declaration needed**: Unlike some languages, Python does not require you to declare variable types
- **Case-sensitive**: `name`, `Name`, and `NAME` are three different variables
- **Multiple assignment**: You can assign values to multiple variables in one line: `x, y, z = 1, 2, 3`
- **Same value to multiple variables**: `a = b = c = 100`
- **Use meaningful names**: Choose names that describe what the variable stores

**Common Mistakes to Avoid:**
- Starting variable names with numbers: `1st_place` (invalid)
- Using spaces in names: `first name` (invalid - use `first_name`)
- Using Python keywords: `for = 5` (invalid)
- Inconsistent naming: mixing `camelCase` and `snake_case`

---

## Practical Examples

### Example 1: Creating Simple Variables

```python
# Integer variable
age = 30

# Float variable
height = 5.9

# String variable
name = "John"

# Boolean variable
is_student = False

print(age)        # Output: 30
print(height)     # Output: 5.9
print(name)       # Output: John
print(is_student) # Output: False
```

### Example 2: Variable Reassignment

```python
# Initial assignment
score = 100
print(score)  # Output: 100

# Reassigning a new value
score = 250
print(score)  # Output: 250

# Changing the type
score = "High"
print(score)  # Output: High
```

### Example 3: Multiple Assignment

```python
# Assigning multiple variables at once
x, y, z = 5, 10, 15
print(x)  # Output: 5
print(y)  # Output: 10
print(z)  # Output: 15

# Assigning the same value to multiple variables
a = b = c = 50
print(a, b, c)  # Output: 50 50 50
```

### Example 4: Using Variables in Calculations

```python
# Store values in variables
price = 20
quantity = 3

# Calculate total
total = price * quantity
print("Total cost:", total)  # Output: Total cost: 60
```

### Example 5: Working with Strings

```python
first_name = "Alice"
last_name = "Smith"

# Combining strings
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith
```

---

## Summary

Variables are essential containers for storing data in Python. They have names and values, and Python's dynamic typing means you do not need to declare types explicitly. Following proper naming conventions and understanding how to create, assign, and reassign variables is fundamental to Python programming.

**Key Takeaways:**
- Variables store data values with descriptive names
- Python is dynamically typed (no type declaration required)
- Variable names must follow specific rules and conventions
- Variables can be reassigned to different values and types
- Use meaningful, descriptive names for clarity

---

## Quick Reference

### Valid Variable Names
```python
age = 25
_count = 10
firstName = "Alice"
student_2 = "Bob"
```

### Invalid Variable Names
```python
2nd_place = "Gold"    # Cannot start with a number
first-name = "Alice"  # Cannot use hyphens
my name = "Bob"       # Cannot contain spaces
for = 10              # Cannot use Python keywords
```

### Checking Variable Type
```python
x = 10
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
```

---

## Review Questions

1. **What is a variable in Python?**
   - Answer: A variable is a named location in memory that stores a data value.

2. **Do you need to declare the type of a variable in Python?**
   - Answer: No, Python is dynamically typed, so you do not need to declare variable types.

3. **Which of the following is a valid variable name?**
   - a) `2students`
   - b) `student_name`
   - c) `student-name`
   - d) `for`
   - Answer: b) `student_name`

4. **What happens if you reassign a variable to a different type?**
   - Answer: Python allows this. The variable will hold the new value and type.

5. **What is the output of the following code?**
   ```python
   x = 5
   x = x + 3
   print(x)
   ```
   - Answer: `8`

6. **How do you assign the same value to multiple variables in one line?**
   - Answer: `a = b = c = value`

7. **Is Python case-sensitive when it comes to variable names?**
   - Answer: Yes, `name` and `Name` are different variables.

8. **What function can you use to check the type of a variable?**
   - Answer: `type()` function

---

## Further Study

**Related Topics:**
- Data types in depth (integers, floats, strings, booleans)
- Type conversion (casting)
- Constants in Python
- Global vs. local variables

**Recommended Resources:**
- Python Variables - W3Schools: https://www.w3schools.com/python/python_variables.asp
- Python Data Types - Real Python: https://realpython.com/python-data-types/
- Python Variables - GeeksforGeeks: https://www.geeksforgeeks.org/python-variables/

**Next Steps:**
- Proceed to Lesson 3: Operators in Python
- Practice creating variables with different data types
- Experiment with variable reassignment
