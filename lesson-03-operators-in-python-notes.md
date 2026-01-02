# Lesson 3: Operators in Python

## Overview

Operators are special symbols in Python that perform operations on values and variables. They enable you to perform calculations, compare values, combine conditions, and manipulate data. Understanding operators is essential for writing functional Python programs.

**Learning Objectives:**
- Understand what operators are and their purpose
- Learn about different types of operators in Python
- Practice using arithmetic, assignment, and logical operators
- Combine operators to create complex expressions

---

## Video Tutorial

Watch the video lesson for this topic:

<iframe width="560" height="315" src="https://www.youtube.com/embed/geCtPFTyVCM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Direct Link:** [Watch on YouTube](https://youtu.be/geCtPFTyVCM)

---

## Key Concepts

### What is an Operator?

An **operator** is a symbol that tells Python to perform a specific operation on one or more values (called operands).

**Example:**
```python
result = 5 + 3  # '+' is the operator, 5 and 3 are operands
```

### Types of Operators in Python

1. **Arithmetic Operators** - Perform mathematical calculations
2. **Assignment Operators** - Assign values to variables
3. **Comparison Operators** - Compare values (covered in Lesson 4)
4. **Logical Operators** - Combine conditional statements
5. **Identity Operators** - Compare object identity
6. **Membership Operators** - Test membership in sequences

---

## Detailed Explanations

### 1. Arithmetic Operators

Arithmetic operators perform basic mathematical operations.

| Operator | Name | Description | Example | Result |
|----------|------|-------------|---------|--------|
| `+` | Addition | Adds two values | `5 + 3` | `8` |
| `-` | Subtraction | Subtracts right from left | `10 - 4` | `6` |
| `*` | Multiplication | Multiplies two values | `6 * 2` | `12` |
| `/` | Division | Divides left by right (float result) | `15 / 4` | `3.75` |
| `//` | Floor Division | Divides and rounds down | `15 // 4` | `3` |
| `%` | Modulus | Returns remainder | `17 % 5` | `2` |
| `**` | Exponentiation | Raises to power | `2 ** 3` | `8` |

### 2. Assignment Operators

Assignment operators assign values to variables.

| Operator | Example | Equivalent To | Description |
|----------|---------|---------------|-------------|
| `=` | `x = 5` | `x = 5` | Assigns value |
| `+=` | `x += 3` | `x = x + 3` | Add and assign |
| `-=` | `x -= 2` | `x = x - 2` | Subtract and assign |
| `*=` | `x *= 4` | `x = x * 4` | Multiply and assign |
| `/=` | `x /= 2` | `x = x / 2` | Divide and assign |
| `//=` | `x //= 3` | `x = x // 3` | Floor divide and assign |
| `%=` | `x %= 5` | `x = x % 5` | Modulus and assign |
| `**=` | `x **= 2` | `x = x ** 2` | Exponent and assign |

### 3. Logical Operators

Logical operators combine conditional statements.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns True if both are True | `True and False` | `False` |
| `or` | Returns True if at least one is True | `True or False` | `True` |
| `not` | Reverses the result | `not True` | `False` |

### 4. Identity Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Returns True if both variables are the same object | `x is y` |
| `is not` | Returns True if variables are not the same object | `x is not y` |

### 5. Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Returns True if value exists in sequence | `"a" in "apple"` → `True` |
| `not in` | Returns True if value does not exist | `"z" not in "apple"` → `True` |

---

## Important Points to Remember

- **Division always returns a float**: `10 / 2` returns `5.0`, not `5`
- **Floor division returns an integer**: `10 // 3` returns `3`
- **Modulus gives remainder**: Useful for checking even/odd numbers
- **Operator precedence matters**: Multiplication and division before addition and subtraction
- **Use parentheses** to control order of operations: `(5 + 3) * 2`

**Common Mistakes to Avoid:**
- Confusing `=` (assignment) with `==` (comparison)
- Forgetting operator precedence rules
- Using `/` when you need `//` for integer division
- Mixing up `and`/`or` logic

---

## Practical Examples

### Example 1: Arithmetic Operators

```python
# Basic arithmetic
a = 15
b = 4

print(a + b)   # Output: 19
print(a - b)   # Output: 11
print(a * b)   # Output: 60
print(a / b)   # Output: 3.75
print(a // b)  # Output: 3 (floor division)
print(a % b)   # Output: 3 (remainder)
print(a ** 2)  # Output: 225 (15 squared)
```

### Example 2: Assignment Operators

```python
# Using compound assignment
x = 10
print(x)      # Output: 10

x += 5        # Same as x = x + 5
print(x)      # Output: 15

x *= 2        # Same as x = x * 2
print(x)      # Output: 30

x //= 4       # Same as x = x // 4
print(x)      # Output: 7
```

### Example 3: Logical Operators

```python
# Combining conditions
age = 25
has_license = True

# Using 'and' - both must be True
can_drive = age >= 18 and has_license
print(can_drive)  # Output: True

# Using 'or' - at least one must be True
is_eligible = age < 18 or age > 65
print(is_eligible)  # Output: False

# Using 'not' - reverses the result
is_not_adult = not (age >= 18)
print(is_not_adult)  # Output: False
```

### Example 4: Membership Operators

```python
# Checking membership
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # Output: True
print("grape" in fruits)      # Output: False
print("grape" not in fruits)  # Output: True

# With strings
message = "Hello World"
print("World" in message)     # Output: True
```

### Example 5: Operator Precedence

```python
# Without parentheses
result1 = 5 + 3 * 2
print(result1)  # Output: 11 (multiplication first)

# With parentheses
result2 = (5 + 3) * 2
print(result2)  # Output: 16 (addition first due to parentheses)
```

### Example 6: Practical Use Case - Calculator

```python
# Simple calculator
num1 = 20
num2 = 5

print("Addition:", num1 + num2)        # Output: 25
print("Subtraction:", num1 - num2)     # Output: 15
print("Multiplication:", num1 * num2)  # Output: 100
print("Division:", num1 / num2)        # Output: 4.0
print("Power:", num1 ** 2)             # Output: 400
```

---

## Summary

Operators are essential tools in Python that allow you to perform operations on data. Arithmetic operators handle mathematical calculations, assignment operators efficiently update variables, logical operators combine conditions, and membership operators check for values in sequences. Understanding operator precedence and proper usage is critical for writing correct programs.

**Key Takeaways:**
- Arithmetic operators perform mathematical operations (+, -, *, /, //, %, **)
- Assignment operators provide shortcuts for updating variables (+=, -=, *=, etc.)
- Logical operators combine Boolean expressions (and, or, not)
- Membership operators check if values exist in sequences (in, not in)
- Operator precedence determines the order of operations
- Use parentheses to explicitly control evaluation order

---

## Quick Reference

### Operator Precedence (High to Low)
1. `**` (Exponentiation)
2. `*`, `/`, `//`, `%` (Multiplication, Division, Floor Division, Modulus)
3. `+`, `-` (Addition, Subtraction)
4. Comparison operators (`==`, `!=`, `<`, `>`, etc.)
5. `not` (Logical NOT)
6. `and` (Logical AND)
7. `or` (Logical OR)

### Common Patterns
```python
# Even number check
is_even = num % 2 == 0

# Increment by 1
count += 1

# Check range
in_range = value >= 0 and value <= 100

# Swap values
a, b = b, a
```

---

## Review Questions

1. **What is the result of `17 % 5`?**
   - Answer: `2` (remainder when 17 is divided by 5)

2. **What is the difference between `/` and `//`?**
   - Answer: `/` performs regular division returning a float, while `//` performs floor division returning an integer.

3. **What does the `+=` operator do?**
   - Answer: It adds the right operand to the left operand and assigns the result to the left operand (`x += 5` is equivalent to `x = x + 5`).

4. **What is the output of `True and False`?**
   - Answer: `False`

5. **What is the output of `True or False`?**
   - Answer: `True`

6. **How do you check if a value exists in a list?**
   - Answer: Use the `in` operator (e.g., `value in list_name`)

7. **What is the result of `2 ** 4`?**
   - Answer: `16` (2 raised to the power of 4)

8. **What is the result of `10 + 5 * 2`?**
   - Answer: `20` (multiplication happens before addition)

9. **How can you ensure addition happens before multiplication in the expression `10 + 5 * 2`?**
   - Answer: Use parentheses: `(10 + 5) * 2` which results in `30`

---

## Further Study

**Related Topics:**
- Operator precedence and associativity
- Bitwise operators
- Comparison operators (Lesson 4)
- Boolean logic (Lesson 6)

**Recommended Resources:**
- Python Operators - W3Schools: https://www.w3schools.com/python/python_operators.asp
- Python Operators - Real Python: https://realpython.com/python-operators-expressions/
- Operator Precedence - Python Documentation: https://docs.python.org/3/reference/expressions.html#operator-precedence

**Next Steps:**
- Proceed to Lesson 4: Comparison Operators and Decision Making
- Practice writing expressions using different operators
- Experiment with operator precedence
