# Lesson 4: Comparison Operators and Decision Making

## Overview

Comparison operators allow you to compare values and make decisions in your programs. They return Boolean values (True or False) that form the foundation of decision-making logic in Python. Understanding comparison operators is essential for controlling program flow based on conditions.

**Learning Objectives:**
- Understand what comparison operators are and how they work
- Learn the different types of comparison operators in Python
- Use comparison operators to create Boolean expressions
- Apply comparisons in decision-making scenarios

---

## Video Tutorial

Watch the video lesson for this topic:

https://www.youtube.com/embed/Qo3Lbp-I9yc

**Direct Link:** [Watch on YouTube](https://youtu.be/Qo3Lbp-I9yc)

---

## Key Concepts

### What are Comparison Operators?

**Comparison operators** (also called relational operators) compare two values and return a Boolean result: `True` or `False`.

**Example:**
```python
5 > 3  # Returns True because 5 is greater than 3
```

### The Six Comparison Operators

Python provides six main comparison operators:

| Operator | Name | Description | Example | Result |
|----------|------|-------------|---------|--------|
| `==` | Equal to | Checks if values are equal | `5 == 5` | `True` |
| `!=` | Not equal to | Checks if values are different | `5 != 3` | `True` |
| `>` | Greater than | Left value is larger | `10 > 7` | `True` |
| `<` | Less than | Left value is smaller | `3 < 8` | `True` |
| `>=` | Greater than or equal to | Left is larger or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal to | Left is smaller or equal | `4 <= 6` | `True` |

---

## Detailed Explanations

### How Comparison Operators Work

Comparison operators evaluate an expression and return a Boolean value:

```python
result = 10 > 5
print(result)  # Output: True
```

### Comparing Different Data Types

**Numbers:**
```python
print(15 > 10)    # True
print(7.5 < 3.2)  # False
```

**Strings:**
Strings are compared alphabetically (lexicographically):
```python
print("apple" < "banana")  # True (a comes before b)
print("Alice" == "alice")  # False (case-sensitive)
```

**Important Note:** You should avoid comparing incompatible types (e.g., number with string) as this may cause errors or unexpected behavior.

### Using Comparisons in Decision Making

Comparison operators are typically used with conditional statements (if, elif, else) to control program flow based on conditions:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

---

## Important Points to Remember

- **`==` vs `=`**:
  - `=` is assignment: `x = 5` (assigns 5 to x)
  - `==` is comparison: `x == 5` (checks if x equals 5)

- **Case sensitivity**: String comparisons are case-sensitive
  - `"Hello" == "hello"` returns `False`

- **Chaining comparisons**: Python allows chaining: `1 < x < 10`

- **Comparing floats**: Be cautious with float comparisons due to precision issues

**Common Mistakes to Avoid:**
- Using `=` instead of `==` for comparison
- Forgetting that string comparisons are case-sensitive
- Comparing incompatible data types
- Assuming `"10" == 10` (string vs. integer) is `True` (it is `False`)

---

## Practical Examples

### Example 1: Basic Comparisons

```python
# Numeric comparisons
print(10 == 10)   # Output: True
print(5 != 3)     # Output: True
print(15 > 20)    # Output: False
print(7 < 12)     # Output: True
print(10 >= 10)   # Output: True
print(5 <= 4)     # Output: False
```

### Example 2: String Comparisons

```python
# Comparing strings
name1 = "Alice"
name2 = "Bob"

print(name1 == "Alice")     # Output: True
print(name1 == "alice")     # Output: False (case-sensitive)
print(name1 != name2)       # Output: True
print("apple" < "banana")   # Output: True (alphabetical order)
```

### Example 3: Using Comparisons with Variables

```python
# Age verification
age = 17
adult_age = 18

is_adult = age >= adult_age
print(is_adult)  # Output: False

# Price comparison
price = 25.99
budget = 30.00

can_afford = price <= budget
print(can_afford)  # Output: True
```

### Example 4: Chaining Comparisons

```python
# Check if a number is within a range
score = 75

# Traditional approach
in_range = score >= 0 and score <= 100
print(in_range)  # Output: True

# Python chaining (more concise)
in_range = 0 <= score <= 100
print(in_range)  # Output: True
```

### Example 5: Practical Use Case - Grade Checker

```python
# Determine if a student passed
passing_grade = 50
student_score = 68

passed = student_score >= passing_grade
print("Passed:", passed)  # Output: Passed: True

# Check for excellence
excellent_grade = 90
is_excellent = student_score >= excellent_grade
print("Excellent:", is_excellent)  # Output: Excellent: False
```

### Example 6: Password Verification

```python
# Simple password check
stored_password = "secure123"
user_input = "secure123"

password_correct = user_input == stored_password
print("Access granted:", password_correct)  # Output: Access granted: True
```

### Example 7: Temperature Monitoring

```python
# Check temperature conditions
current_temp = 28
max_temp = 30
min_temp = 15

is_too_hot = current_temp > max_temp
is_too_cold = current_temp < min_temp
is_comfortable = min_temp <= current_temp <= max_temp

print("Too hot:", is_too_hot)           # Output: Too hot: False
print("Too cold:", is_too_cold)         # Output: Too cold: False
print("Comfortable:", is_comfortable)   # Output: Comfortable: True
```

---

## Summary

Comparison operators are fundamental tools for decision-making in Python. They compare values and return Boolean results (True or False) that enable programs to respond to different conditions. The six comparison operators (==, !=, >, <, >=, <=) can be used with numbers, strings, and other data types to create logical expressions that control program flow.

**Key Takeaways:**
- Comparison operators compare values and return `True` or `False`
- Six main operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Never confuse `=` (assignment) with `==` (comparison)
- String comparisons are case-sensitive and alphabetical
- Python allows chaining comparisons for range checks
- Comparisons form the foundation for conditional statements

---

## Quick Reference

### All Comparison Operators
```python
# Equal to
5 == 5          # True

# Not equal to
5 != 3          # True

# Greater than
10 > 7          # True

# Less than
3 < 8           # True

# Greater than or equal to
5 >= 5          # True

# Less than or equal to
4 <= 6          # True
```

### Common Patterns
```python
# Check if in range
valid = 0 <= value <= 100

# Check if equal (case-insensitive)
match = name.lower() == "alice"

# Check if not equal
different = x != y

# Multiple conditions
eligible = age >= 18 and score > 50
```

---

## Review Questions

1. **What is the difference between `=` and `==`?**
   - Answer: `=` is the assignment operator (assigns values), while `==` is the comparison operator (checks equality).

2. **What does the expression `10 >= 10` return?**
   - Answer: `True` (10 is equal to 10, satisfying the "greater than or equal to" condition)

3. **Is `"Apple" == "apple"` True or False?**
   - Answer: `False` (string comparisons are case-sensitive)

4. **What is the result of `5 != 5`?**
   - Answer: `False` (5 is equal to 5, not different)

5. **How would you check if a variable `x` is between 10 and 20 (inclusive)?**
   - Answer: `10 <= x <= 20`

6. **What does `"cat" < "dog"` return?**
   - Answer: `True` (c comes before d alphabetically)

7. **Write a comparison to check if a temperature is above freezing (0°C).**
   - Answer: `temperature > 0`

8. **What is returned by comparison operators?**
   - Answer: Boolean values (`True` or `False`)

9. **Can you use `>=` with strings?**
   - Answer: Yes, strings are compared alphabetically.

---

## Further Study

**Related Topics:**
- Boolean logic and Boolean values (Lesson 6)
- Conditional statements: if, elif, else (Lesson 7)
- Logical operators (and, or, not)
- Truthy and falsy values in Python

**Recommended Resources:**
- Python Comparison Operators - W3Schools: https://www.w3schools.com/python/python_operators.asp
- Python Comparisons - Real Python: https://realpython.com/python-operators-expressions/
- Python if...else - Programiz: https://www.programiz.com/python-programming/if-elif-else

**Next Steps:**
- Proceed to Lesson 5: Python Conversation - Print, Input, and f-Strings
- Practice writing comparison expressions
- Experiment with different data types in comparisons
- Prepare for combining comparisons with conditional statements
