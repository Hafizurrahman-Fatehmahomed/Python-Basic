# Lesson 6: Python Booleans - The Logic of True and False

## Overview

Booleans are a fundamental data type in Python that represent truth values: `True` or `False`. They form the foundation of logical operations and decision-making in programming. Understanding Booleans is essential for controlling program flow and implementing conditional logic.

**Learning Objectives:**
- Understand what Booleans are and their importance
- Learn how to create and use Boolean values
- Explore truthy and falsy values in Python
- Master Boolean logic with logical operators
- Apply Booleans in conditional statements

---

## Video Tutorial

Watch the video lesson for this topic:

https://www.youtube.com/embed/eibvXWy33sI

**Direct Link:** [Watch on YouTube](https://youtu.be/eibvXWy33sI)

---

## Key Concepts

### What is a Boolean?

A **Boolean** is a data type that has only two possible values: `True` or `False`. Named after mathematician George Boole, Booleans represent the truth or falsehood of a statement.

**Important Note:** In Python, Boolean values are capitalized: `True` and `False` (not `true` or `false`).

### Boolean Values

```python
is_active = True
is_complete = False
```

### Boolean Results

Booleans are commonly returned by:
- Comparison operations (`5 > 3` returns `True`)
- Logical operations (`True and False` returns `False`)
- Boolean functions (`isinstance()`, `hasattr()`, etc.)

---

## Detailed Explanations

### 1. Creating Boolean Values

**Direct Assignment:**
```python
is_student = True
has_license = False
```

**From Comparisons:**
```python
is_adult = age >= 18  # Returns True or False
```

**Using `bool()` Function:**
```python
result = bool(1)    # True
result = bool(0)    # False
result = bool("")   # False
```

### 2. Logical Operators

Logical operators combine or modify Boolean values:

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns `True` if both are `True` | `True and False` | `False` |
| `or` | Returns `True` if at least one is `True` | `True or False` | `True` |
| `not` | Reverses the Boolean value | `not True` | `False` |

### 3. Truthy and Falsy Values

Python treats certain values as `True` or `False` in Boolean contexts:

**Falsy Values (evaluate to `False`):**
- `False`
- `0` (zero)
- `0.0` (zero float)
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dictionary)
- `None`

**Truthy Values (evaluate to `True`):**
- `True`
- Any non-zero number (`1`, `-5`, `3.14`)
- Any non-empty string (`"text"`, `"0"`)
- Any non-empty collection (`[1, 2]`, `{"a": 1}`)

### 4. Truth Tables

**AND Operator:**
| A | B | A and B |
|-------|-------|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**OR Operator:**
| A | B | A or B |
|-------|-------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**NOT Operator:**
| A | not A |
|-------|-------|
| True | False |
| False | True |

---

## Important Points to Remember

- **Capitalization matters**: Use `True` and `False`, not `true` or `false`
- **`and` requires both**: Both conditions must be `True`
- **`or` requires at least one**: At least one condition must be `True`
- **`not` reverses**: Flips `True` to `False` and vice versa
- **Short-circuit evaluation**: `and` stops at first `False`, `or` stops at first `True`
- **Empty collections are falsy**: Empty strings, lists, etc., evaluate to `False`

**Common Mistakes to Avoid:**
- Writing `true` instead of `True` (causes NameError)
- Confusing `and`/`or` with `&`/`|` (bitwise operators)
- Using `=` instead of `==` in comparisons
- Forgetting operator precedence: `not` > `and` > `or`

---

## Practical Examples

### Example 1: Basic Boolean Values

```python
# Direct Boolean values
is_raining = True
is_sunny = False

print(is_raining)  # Output: True
print(is_sunny)    # Output: False
print(type(is_raining))  # Output: <class 'bool'>
```

### Example 2: Booleans from Comparisons

```python
age = 20
height = 175

is_adult = age >= 18
is_tall = height > 180

print(is_adult)  # Output: True
print(is_tall)   # Output: False
```

### Example 3: Logical Operators - `and`

```python
# Both conditions must be True
has_ticket = True
has_id = True

can_enter = has_ticket and has_id
print(can_enter)  # Output: True

# If one is False
has_ticket = True
has_id = False
can_enter = has_ticket and has_id
print(can_enter)  # Output: False
```

### Example 4: Logical Operators - `or`

```python
# At least one condition must be True
is_weekend = False
is_holiday = True

is_day_off = is_weekend or is_holiday
print(is_day_off)  # Output: True

# Both False
is_weekend = False
is_holiday = False
is_day_off = is_weekend or is_holiday
print(is_day_off)  # Output: False
```

### Example 5: Logical Operator - `not`

```python
# Reverses the Boolean value
is_logged_in = False
is_logged_out = not is_logged_in

print(is_logged_out)  # Output: True

# Double negative
is_active = True
is_not_active = not is_active
print(is_not_active)  # Output: False
```

### Example 6: Truthy and Falsy Values

```python
# Testing falsy values
print(bool(0))       # Output: False
print(bool(""))      # Output: False
print(bool([]))      # Output: False
print(bool(None))    # Output: False

# Testing truthy values
print(bool(1))       # Output: True
print(bool("hello")) # Output: True
print(bool([1, 2]))  # Output: True
print(bool(-5))      # Output: True
```

### Example 7: Combining Multiple Conditions

```python
# Checking eligibility for a loan
age = 25
income = 50000
has_debt = False

is_eligible = age >= 21 and income >= 30000 and not has_debt
print(is_eligible)  # Output: True
```

### Example 8: Complex Boolean Logic

```python
# Checking if a student passes
homework_done = True
attendance = 85
exam_score = 72

passed = homework_done and attendance >= 75 and exam_score >= 60
print(f"Student passed: {passed}")  # Output: Student passed: True
```

### Example 9: Practical Use Case - Access Control

```python
# Determining access rights
is_admin = False
is_owner = True
is_member = True

# Access granted if admin OR (owner AND member)
has_access = is_admin or (is_owner and is_member)
print(f"Access granted: {has_access}")  # Output: Access granted: True
```

### Example 10: Password Validation

```python
# Simple password validation
password = "secure123"
confirm_password = "secure123"

min_length = 8
has_numbers = any(char.isdigit() for char in password)

passwords_match = password == confirm_password
is_long_enough = len(password) >= min_length

is_valid = passwords_match and is_long_enough and has_numbers
print(f"Password is valid: {is_valid}")  # Output: Password is valid: True
```

---

## Summary

Booleans are a fundamental data type in Python representing `True` or `False` values. They are essential for decision-making and controlling program flow. Logical operators (`and`, `or`, `not`) allow you to combine and manipulate Boolean values. Understanding truthy and falsy values enables you to write more concise conditional statements.

**Key Takeaways:**
- Booleans have only two values: `True` and `False` (capitalized)
- Comparison operations return Boolean values
- Logical operators: `and` (both), `or` (at least one), `not` (reverse)
- Empty values (0, "", [], etc.) are falsy; non-empty values are truthy
- Booleans are the foundation of conditional logic and decision-making
- Operator precedence: `not` > `and` > `or`

---

## Quick Reference

### Boolean Values
```python
True                 # Boolean True
False                # Boolean False
bool(value)          # Convert to Boolean
```

### Logical Operators
```python
True and True        # True
True and False       # False
True or False        # True
False or False       # False
not True             # False
not False            # True
```

### Falsy Values
```python
bool(False)          # False
bool(0)              # False
bool("")             # False
bool([])             # False
bool(None)           # False
```

### Truthy Values
```python
bool(True)           # True
bool(1)              # True
bool("text")         # True
bool([1, 2])         # True
```

### Common Patterns
```python
# Check if in range
valid = 0 <= value <= 100

# Check multiple conditions
eligible = age >= 18 and has_id and not is_banned

# Check at least one condition
can_proceed = is_admin or is_moderator or is_owner

# Toggle boolean
is_active = not is_active
```

---

## Review Questions

1. **What are the two possible values of a Boolean in Python?**
   - Answer: `True` and `False`

2. **What is the result of `True and False`?**
   - Answer: `False`

3. **What is the result of `True or False`?**
   - Answer: `True`

4. **What does `not True` return?**
   - Answer: `False`

5. **Is the empty string `""` truthy or falsy?**
   - Answer: Falsy (evaluates to `False`)

6. **What is the result of `bool(0)`?**
   - Answer: `False`

7. **What is the result of `bool("Hello")`?**
   - Answer: `True`

8. **What is the operator precedence for logical operators?**
   - Answer: `not` (highest), then `and`, then `or` (lowest)

9. **Evaluate: `10 > 5 and 3 < 7`**
   - Answer: `True` (both conditions are `True`)

10. **What values are considered falsy in Python?**
    - Answer: `False`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `None`

---

## Further Study

**Related Topics:**
- Comparison operators (Lesson 4)
- Conditional statements: if, elif, else (Lesson 7)
- Boolean algebra and De Morgan's laws
- Short-circuit evaluation

**Recommended Resources:**
- Python Booleans - W3Schools: https://www.w3schools.com/python/python_booleans.asp
- Python Boolean Logic - Real Python: https://realpython.com/python-boolean/
- Truth Value Testing - Python Docs: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

**Next Steps:**
- Proceed to Lesson 7: Decisions in Python - if, elif, and else
- Practice combining Boolean conditions
- Experiment with truthy and falsy values
- Build programs that use Boolean logic for decision-making
