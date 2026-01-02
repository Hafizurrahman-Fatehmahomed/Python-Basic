# Lesson 9: Functions in Python - def and return

## Overview

Functions are reusable blocks of code that perform specific tasks. They help organize code, reduce repetition, and make programs more modular and maintainable. Understanding how to define and use functions with the `def` keyword and `return` statement is essential for writing efficient Python programs.

**Learning Objectives:**
- Understand what functions are and why they are important
- Learn how to define functions using the `def` keyword
- Master parameters and arguments
- Use the `return` statement to send values back
- Apply functions to solve problems efficiently

---

## Video Tutorial

Watch the video lesson for this topic:

https://www.youtube.com/embed/ScwJBuAF66E

**Direct Link:** [Watch on YouTube](https://youtu.be/ScwJBuAF66E)

---

## Key Concepts

### What is a Function?

A **function** is a named block of reusable code that performs a specific task. Functions:
- **Organize code**: Break programs into logical, manageable pieces
- **Reduce repetition**: Write code once, use it many times
- **Improve readability**: Make code easier to understand
- **Enable testing**: Test individual pieces independently

### Function Components

1. **Definition**: Creating the function using `def`
2. **Parameters**: Variables that receive values (optional)
3. **Body**: The code that executes when the function is called
4. **Return**: Sends a value back to the caller (optional)
5. **Call**: Executing the function to perform its task

---

## Detailed Explanations

### 1. Defining a Function

Use the `def` keyword to define a function.

**Syntax:**
```python
def function_name():
    # function body
    statement(s)
```

**Example:**
```python
def greet():
    print("Hello, World!")
```

### 2. Calling a Function

Execute a function by using its name followed by parentheses.

**Syntax:**
```python
function_name()
```

**Example:**
```python
greet()  # Output: Hello, World!
```

### 3. Functions with Parameters

Parameters allow functions to accept input values.

**Syntax:**
```python
def function_name(parameter1, parameter2):
    # use parameters in function body
    statement(s)
```

**Example:**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

**Terminology:**
- **Parameter**: Variable in the function definition (`name`)
- **Argument**: Actual value passed when calling (`"Alice"`)

### 4. The `return` Statement

The `return` statement sends a value back to the caller and exits the function.

**Syntax:**
```python
def function_name():
    # code
    return value
```

**Example:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

**Important Notes:**
- Functions without `return` implicitly return `None`
- `return` immediately exits the function
- Can return any data type: numbers, strings, lists, etc.

### 5. Default Parameters

Provide default values for parameters.

**Syntax:**
```python
def function_name(param1, param2=default_value):
    statement(s)
```

**Example:**
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Output: Hello, Alice!
greet("Bob", "Hi")          # Output: Hi, Bob!
```

### 6. Multiple Return Values

Functions can return multiple values as a tuple.

**Example:**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(minimum, maximum)  # Output: 1 9
```

---

## Important Points to Remember

- **`def` keyword**: Always use `def` to define functions
- **Colon (`:`)**: Required after the function signature
- **Indentation**: Function body must be indented
- **Naming**: Use descriptive names (lowercase with underscores)
- **Parameters vs Arguments**: Parameters in definition, arguments when calling
- **`return` exits**: Code after `return` in the same block will not execute
- **No `return` = `None`**: Functions without `return` return `None` by default

**Common Mistakes to Avoid:**
- Forgetting the colon (`:`) after the function definition
- Incorrect or missing indentation
- Calling a function before defining it
- Forgetting parentheses when calling a function
- Confusing parameters (definition) with arguments (call)
- Not storing or using the returned value

---

## Practical Examples

### Example 1: Simple Function Without Parameters

```python
# Define function
def say_hello():
    print("Hello, World!")

# Call function
say_hello()  # Output: Hello, World!
say_hello()  # Output: Hello, World!
```

### Example 2: Function with One Parameter

```python
# Define function
def greet(name):
    print(f"Welcome, {name}!")

# Call function with different arguments
greet("Alice")   # Output: Welcome, Alice!
greet("Bob")     # Output: Welcome, Bob!
```

### Example 3: Function with Multiple Parameters

```python
# Define function
def introduce(name, age, city):
    print(f"My name is {name}. I am {age} years old and live in {city}.")

# Call function
introduce("Alice", 25, "New York")
# Output: My name is Alice. I am 25 years old and live in New York.
```

### Example 4: Function with Return Value

```python
# Define function that calculates area
def calculate_area(length, width):
    area = length * width
    return area

# Call function and store result
room_area = calculate_area(10, 8)
print(f"Room area: {room_area} square meters")
# Output: Room area: 80 square meters
```

### Example 5: Function with Default Parameters

```python
# Define function with default parameter
def power(base, exponent=2):
    return base ** exponent

# Call with different arguments
print(power(5))       # Output: 25 (5^2)
print(power(5, 3))    # Output: 125 (5^3)
print(power(2, 4))    # Output: 16 (2^4)
```

### Example 6: Function Returning Multiple Values

```python
# Define function that returns multiple values
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Call and unpack returned values
scores = [85, 92, 78, 90]
total_score, avg_score = get_stats(scores)

print(f"Total: {total_score}")
print(f"Average: {avg_score:.1f}")
# Output:
# Total: 345
# Average: 86.2
```

### Example 7: Function with Conditional Logic

```python
# Define function with if-else
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Use function
status1 = check_age(25)
status2 = check_age(15)

print(status1)  # Output: Adult
print(status2)  # Output: Minor
```

### Example 8: Function with List Parameter

```python
# Define function that processes a list
def find_max(numbers):
    if not numbers:  # Check if list is empty
        return None

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Call function
scores = [78, 92, 85, 90, 88]
highest = find_max(scores)
print(f"Highest score: {highest}")  # Output: Highest score: 92
```

### Example 9: Temperature Converter

```python
# Define conversion functions
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Use functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # Output: 25°C = 77.0°F

temp_f2 = 98.6
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2:.1f}°C")  # Output: 98.6°F = 37.0°C
```

### Example 10: Calculator Functions

```python
# Define calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Use calculator functions
print(f"10 + 5 = {add(10, 5)}")           # Output: 10 + 5 = 15
print(f"10 - 5 = {subtract(10, 5)}")      # Output: 10 - 5 = 5
print(f"10 × 5 = {multiply(10, 5)}")      # Output: 10 × 5 = 50
print(f"10 ÷ 5 = {divide(10, 5)}")        # Output: 10 ÷ 5 = 2.0
print(f"10 ÷ 0 = {divide(10, 0)}")        # Output: 10 ÷ 0 = Error: Division by zero
```

### Example 11: Validation Function

```python
# Define validation function
def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one number
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        return False

    return True

# Test function
password1 = "secure123"
password2 = "short"

print(f"Password '{password1}' is valid: {is_valid_password(password1)}")
# Output: Password 'secure123' is valid: True

print(f"Password '{password2}' is valid: {is_valid_password(password2)}")
# Output: Password 'short' is valid: False
```

### Example 12: Interactive Program with Functions

```python
# Define helper functions
def get_user_choice():
    print("\n=== Menu ===")
    print("1. Calculate area")
    print("2. Calculate perimeter")
    choice = input("Enter choice (1 or 2): ")
    return choice

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Main program
choice = get_user_choice()
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if choice == "1":
    area = calculate_rectangle_area(length, width)
    print(f"Area: {area} square units")
elif choice == "2":
    perimeter = calculate_rectangle_perimeter(length, width)
    print(f"Perimeter: {perimeter} units")
else:
    print("Invalid choice")
```

---

## Summary

Functions are fundamental building blocks in Python that enable code reusability, organization, and modularity. They are defined using the `def` keyword, can accept parameters, perform operations, and return values using the `return` statement. Mastering functions is essential for writing clean, efficient, and maintainable Python code.

**Key Takeaways:**
- Functions are defined using `def function_name():`
- Parameters allow functions to accept input values
- Arguments are the actual values passed when calling functions
- `return` statement sends values back to the caller
- Functions without `return` implicitly return `None`
- Default parameters provide fallback values
- Functions can return multiple values as tuples
- Use descriptive names and follow Python naming conventions

---

## Quick Reference

### Basic Function Syntax
```python
# Simple function
def function_name():
    statement(s)

# With parameters
def function_name(param1, param2):
    statement(s)

# With return
def function_name(param):
    return value

# With default parameter
def function_name(param1, param2=default):
    return value
```

### Calling Functions
```python
function_name()                    # No parameters
function_name(arg1, arg2)          # With arguments
result = function_name(arg)        # Store return value
```

### Common Patterns
```python
# Return calculation
def calculate(x, y):
    return x + y

# Return based on condition
def classify(value):
    if value > 0:
        return "positive"
    else:
        return "non-positive"

# Multiple returns
def get_both():
    return value1, value2

# Default parameters
def greet(name, msg="Hello"):
    return f"{msg}, {name}"
```

---

## Review Questions

1. **What keyword is used to define a function in Python?**
   - Answer: `def`

2. **What is the difference between a parameter and an argument?**
   - Answer: A parameter is a variable in the function definition; an argument is the actual value passed when calling the function.

3. **What does the `return` statement do?**
   - Answer: It sends a value back to the caller and exits the function.

4. **What value does a function return if it has no `return` statement?**
   - Answer: `None`

5. **How do you call a function named `calculate`?**
   - Answer: `calculate()`

6. **What is a default parameter?**
   - Answer: A parameter with a preset value that is used if no argument is provided.

7. **Can a function return multiple values?**
   - Answer: Yes, as a tuple.

8. **What happens to code after a `return` statement in the same block?**
   - Answer: It does not execute (unreachable code).

9. **Write a function that adds two numbers and returns the result.**
   - Answer:
     ```python
     def add(a, b):
         return a + b
     ```

10. **What is the output of the following code?**
    ```python
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    print(result)
    ```
    - Answer: `20`

---

## Further Study

**Related Topics:**
- Lambda functions (anonymous functions)
- Scope and lifetime of variables (local vs global)
- Recursion (functions calling themselves)
- Docstrings (documenting functions)
- `*args` and `**kwargs` (variable-length arguments)
- Function annotations and type hints

**Recommended Resources:**
- Python Functions - Official Docs: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Python Functions - W3Schools: https://www.w3schools.com/python/python_functions.asp
- Python Functions - Real Python: https://realpython.com/defining-your-own-python-function/
- Python Functions - Programiz: https://www.programiz.com/python-programming/function

**Next Steps:**
- Practice writing functions for different tasks
- Experiment with different parameter configurations
- Build programs that use multiple functions working together
- Explore more advanced function concepts like recursion and decorators

---

## Congratulations!

You have completed all 9 Python lessons! You now have a solid foundation in:
1. What Python is and its uses
2. Variables and data types
3. Operators for calculations and logic
4. Comparison operators and decision-making
5. Input/output with print, input, and f-strings
6. Boolean logic and truth values
7. Conditional statements (if, elif, else)
8. Lists for storing collections
9. Functions for code organization and reusability

**Continue practicing** by building small projects and experimenting with these concepts. The more you code, the more comfortable you will become with Python!
