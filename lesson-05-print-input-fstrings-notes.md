# Lesson 5: Python Conversation - Print, Input, and f-Strings

## Overview

Communication between your program and users is essential in programming. Python provides powerful tools for displaying output (`print()`), receiving input (`input()`), and formatting strings (`f-strings`). These functions enable interactive programs that can display information and respond to user input.

**Learning Objectives:**
- Understand how to use the `print()` function to display output
- Learn how to use the `input()` function to receive user input
- Master f-strings for elegant string formatting
- Combine these tools to create interactive programs

---

## Video Tutorial

Watch the video lesson for this topic:

<iframe width="560" height="315" src="https://www.youtube.com/embed/TvBR0Y6toNM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Direct Link:** [Watch on YouTube](https://youtu.be/TvBR0Y6toNM)

---

## Key Concepts

### The `print()` Function

The **`print()`** function displays output to the console (screen).

**Syntax:**
```python
print(value1, value2, ...)
```

### The `input()` Function

The **`input()`** function reads text input from the user and returns it as a string.

**Syntax:**
```python
variable = input("prompt message")
```

### f-Strings (Formatted String Literals)

**f-strings** provide a concise and readable way to embed expressions inside string literals using curly braces `{}`.

**Syntax:**
```python
f"Text {variable} more text"
```

---

## Detailed Explanations

### 1. The `print()` Function

The `print()` function is used to display information to the user.

**Basic Usage:**
```python
print("Hello, World!")
```

**Features:**
- Print multiple values separated by commas
- Automatically adds a space between values
- Adds a newline at the end by default
- Can customize separator with `sep` parameter
- Can customize ending with `end` parameter

### 2. The `input()` Function

The `input()` function pauses program execution and waits for the user to type something and press Enter.

**Important Notes:**
- Always returns a **string**, even if the user enters a number
- Use type conversion to convert input to other types (int, float, etc.)
- The prompt message is optional but recommended

### 3. f-Strings (Formatted String Literals)

Introduced in Python 3.6, f-strings are the modern, preferred way to format strings.

**Advantages:**
- More readable than older methods (`%` formatting, `.format()`)
- Faster performance
- Can embed expressions directly inside strings
- Supports formatting specifications

**Syntax:**
- Place `f` or `F` before the opening quote
- Use `{}` to embed variables or expressions

---

## Important Points to Remember

- **`input()` always returns a string**: Convert to numbers using `int()` or `float()` if needed
- **f-strings require Python 3.6+**: Use the `f` prefix before the string
- **`print()` parameters**:
  - `sep`: Separator between multiple values (default: space)
  - `end`: What to print at the end (default: newline `\n`)
- **Expressions in f-strings**: You can perform calculations or call functions inside `{}`

**Common Mistakes to Avoid:**
- Forgetting to convert `input()` to int/float when doing math
- Missing the `f` prefix in f-strings
- Using quotes incorrectly inside f-strings
- Not providing a clear prompt message in `input()`

---

## Practical Examples

### Example 1: Basic `print()` Usage

```python
# Simple print
print("Hello, World!")
# Output: Hello, World!

# Printing variables
name = "Alice"
print(name)
# Output: Alice

# Printing multiple values
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25
```

### Example 2: `print()` with Custom Separator and Ending

```python
# Custom separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

# Custom ending (no newline)
print("Loading", end="...")
print("Done!")
# Output: Loading...Done!

# Combining sep and end
print("Python", "is", "awesome", sep="-", end="!\n")
# Output: Python-is-awesome!
```

### Example 3: Basic `input()` Usage

```python
# Getting user input
name = input("What is your name? ")
print("Hello,", name)

# Example interaction:
# What is your name? Bob
# Hello, Bob
```

### Example 4: Converting Input to Numbers

```python
# Input returns a string, so we need to convert
age_str = input("Enter your age: ")
age = int(age_str)  # Convert string to integer

# Shorter version
age = int(input("Enter your age: "))

# Example
years_until_30 = 30 - age
print("Years until 30:", years_until_30)
```

### Example 5: Basic f-Strings

```python
# Simple f-string
name = "Alice"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)
# Output: My name is Alice and I am 25 years old.
```

### Example 6: f-Strings with Expressions

```python
# Calculations inside f-strings
price = 19.99
quantity = 3

print(f"Total cost: ${price * quantity}")
# Output: Total cost: $59.97

# Using methods
name = "alice"
print(f"Hello, {name.upper()}!")
# Output: Hello, ALICE!
```

### Example 7: f-Strings with Formatting

```python
# Number formatting
pi = 3.14159265359

print(f"Pi rounded to 2 decimals: {pi:.2f}")
# Output: Pi rounded to 2 decimals: 3.14

# Width and alignment
name = "Bob"
print(f"Name: {name:>10}")  # Right-aligned, width 10
# Output: Name:        Bob
```

### Example 8: Interactive Program - Age Calculator

```python
# Complete interactive program
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year

print(f"Hello, {name}! You are approximately {age} years old.")

# Example interaction:
# What is your name? Sarah
# What year were you born? 2000
# Hello, Sarah! You are approximately 26 years old.
```

### Example 9: Interactive Program - Simple Calculator

```python
# Get two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
sum_result = num1 + num2
product = num1 * num2

# Display results using f-strings
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} × {num2} = {product}")

# Example interaction:
# Enter first number: 5
# Enter second number: 3
# 5.0 + 3.0 = 8.0
# 5.0 × 3.0 = 15.0
```

### Example 10: Combining Everything

```python
# Interactive greeting program
print("=== Welcome to the Greeting Program ===")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Create formatted output
full_name = f"{first_name} {last_name}"
print(f"\nNice to meet you, {full_name}!")
print(f"You are {age} years old.")

# Calculate and display years to milestones
years_to_100 = 100 - age
print(f"You have {years_to_100} years until you turn 100!")
```

---

## Summary

The `print()`, `input()`, and f-strings are fundamental tools for creating interactive Python programs. `print()` displays output to users, `input()` captures user input as strings, and f-strings provide elegant, readable string formatting. Combining these tools allows you to build programs that communicate effectively with users.

**Key Takeaways:**
- `print()` displays output; can print multiple values and customize formatting
- `input()` receives user input as a string; convert to numbers using `int()` or `float()`
- f-strings use the `f` prefix and `{}` to embed variables and expressions
- f-strings are faster and more readable than older formatting methods
- Always provide clear prompts when using `input()`
- Remember to convert input types when performing mathematical operations

---

## Quick Reference

### `print()` Syntax
```python
print(value)                           # Single value
print(value1, value2)                  # Multiple values
print(value1, value2, sep=", ")        # Custom separator
print(value, end="")                   # Custom ending
```

### `input()` Syntax
```python
name = input("Prompt: ")               # String input
age = int(input("Enter age: "))        # Convert to integer
price = float(input("Enter price: "))  # Convert to float
```

### f-String Syntax
```python
f"Text {variable}"                     # Basic
f"Result: {expression}"                # With expression
f"Price: ${price:.2f}"                 # With formatting
f"{value:10}"                          # Width specification
```

### Common Format Specifications
```python
f"{number:.2f}"      # 2 decimal places
f"{number:10}"       # Width of 10
f"{text:>10}"        # Right-aligned
f"{text:<10}"        # Left-aligned
f"{text:^10}"        # Center-aligned
```

---

## Review Questions

1. **What does the `print()` function do?**
   - Answer: It displays output to the console/screen.

2. **What data type does `input()` return?**
   - Answer: String (str)

3. **How do you convert user input to an integer?**
   - Answer: Use `int(input("Prompt: "))`

4. **What is the purpose of the `f` in f-strings?**
   - Answer: It indicates a formatted string literal that can embed expressions using `{}`.

5. **What is the output of `print("A", "B", "C", sep="-")`?**
   - Answer: `A-B-C`

6. **Write an f-string that displays a variable `name` and `age`.**
   - Answer: `f"Name: {name}, Age: {age}"`

7. **How do you prevent `print()` from adding a newline at the end?**
   - Answer: Use `end=""` parameter: `print("text", end="")`

8. **What is the result of `f"{10 + 5}"`?**
   - Answer: `"15"` (the expression is evaluated)

9. **How do you format a float to 2 decimal places using f-strings?**
   - Answer: `f"{value:.2f}"`

---

## Further Study

**Related Topics:**
- String methods (`.upper()`, `.lower()`, `.strip()`, etc.)
- Type conversion functions (`int()`, `float()`, `str()`)
- String concatenation and multiplication
- Advanced f-string formatting options

**Recommended Resources:**
- Python Input/Output - Official Docs: https://docs.python.org/3/tutorial/inputoutput.html
- Python f-Strings - Real Python: https://realpython.com/python-f-strings/
- Python print() Function - W3Schools: https://www.w3schools.com/python/ref_func_print.asp
- Python f-Strings - DataCamp: https://www.datacamp.com/tutorial/python-f-string

**Next Steps:**
- Proceed to Lesson 6: Python Booleans - The Logic of True and False
- Practice creating interactive programs
- Experiment with different f-string formatting options
- Build a simple quiz or questionnaire program
