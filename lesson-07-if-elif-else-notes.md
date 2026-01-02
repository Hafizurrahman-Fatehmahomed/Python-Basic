# Lesson 7: Decisions in Python - if, elif, and else

## Overview

Conditional statements allow your programs to make decisions and execute different code based on conditions. The `if`, `elif`, and `else` statements form the foundation of control flow in Python, enabling programs to respond dynamically to different situations.

**Learning Objectives:**
- Understand how conditional statements control program flow
- Learn the syntax of `if`, `elif`, and `else` statements
- Practice writing single and multi-branch conditionals
- Apply conditional logic to solve real-world problems

---

## Video Tutorial

Watch the video lesson for this topic:

<iframe width="560" height="315" src="https://www.youtube.com/embed/vVXSSVmNmKA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Direct Link:** [Watch on YouTube](https://youtu.be/vVXSSVmNmKA)

---

## Key Concepts

### What are Conditional Statements?

**Conditional statements** allow programs to execute different code blocks based on whether conditions are `True` or `False`.

### The Three Keywords

| Keyword | Purpose | Required? |
|---------|---------|-----------|
| `if` | Tests the first condition | Yes (always required) |
| `elif` | Tests additional conditions (else if) | No (optional) |
| `else` | Executes when all conditions are `False` | No (optional) |

### Basic Structure

```python
if condition:
    # code executed if condition is True
elif another_condition:
    # code executed if another_condition is True
else:
    # code executed if all conditions are False
```

---

## Detailed Explanations

### 1. The `if` Statement

The simplest form tests a single condition.

**Syntax:**
```python
if condition:
    statement(s)
```

**Example:**
```python
age = 20

if age >= 18:
    print("You are an adult")
```

**Important:** The code block must be **indented** (typically 4 spaces or 1 tab).

### 2. The `if-else` Statement

Provides an alternative when the condition is `False`.

**Syntax:**
```python
if condition:
    statement(s)
else:
    statement(s)
```

**Example:**
```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### 3. The `if-elif-else` Statement

Tests multiple conditions in sequence.

**Syntax:**
```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)
```

**How it works:**
1. Python tests `condition1` first
2. If `True`, executes that block and skips the rest
3. If `False`, tests `condition2`, and so on
4. If all conditions are `False`, executes the `else` block (if present)

**Example:**
```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### 4. Nested Conditionals

You can place `if` statements inside other `if` statements.

**Example:**
```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
```

---

## Important Points to Remember

- **Indentation is mandatory**: Python uses indentation to define code blocks
- **Colon (`:`) required**: Each `if`, `elif`, and `else` must end with a colon
- **Only one block executes**: Once a condition is `True`, remaining conditions are skipped
- **`elif` is NOT `else if`**: Python uses `elif`, not `else if`
- **Multiple `elif` allowed**: You can have as many `elif` blocks as needed
- **`else` is always last**: The `else` block, if present, must come after all `if`/`elif` blocks

**Common Mistakes to Avoid:**
- Forgetting the colon (`:`) after conditions
- Incorrect or inconsistent indentation
- Using `=` instead of `==` for comparison
- Writing `else if` instead of `elif`
- Placing `else` before `elif`

---

## Practical Examples

### Example 1: Simple `if` Statement

```python
temperature = 30

if temperature > 25:
    print("It's hot outside!")

# Output: It's hot outside!
```

### Example 2: `if-else` Statement

```python
age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# Output: You cannot vote yet
```

### Example 3: `if-elif-else` Statement - Grade Calculator

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
# Output: Your grade is: B
```

### Example 4: Multiple Conditions with Logical Operators

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome to the concert!")
elif age >= 18 and not has_ticket:
    print("Please buy a ticket first")
else:
    print("Sorry, you must be 18 or older")
```

### Example 5: Nested Conditionals - Login System

```python
username = "admin"
password = "secure123"

user_input = "admin"
pass_input = "secure123"

if user_input == username:
    if pass_input == password:
        print("Login successful!")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Output: Login successful!
```

### Example 6: Checking Number Properties

```python
number = 12

if number > 0:
    print("Positive number")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Output:
# Positive number
# Even number
```

### Example 7: Temperature Advisory System

```python
temperature = 28

if temperature > 30:
    print("It's very hot. Stay hydrated!")
elif temperature > 20:
    print("Nice weather!")
elif temperature > 10:
    print("It's a bit cool. Wear a jacket.")
else:
    print("It's cold. Bundle up!")

# Output: Nice weather!
```

### Example 8: Interactive Age Classifier

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")

# Example interaction:
# Enter your age: 25
# You are an adult
```

### Example 9: BMI Calculator with Recommendations

```python
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.1f} - Underweight")
elif bmi < 25:
    print(f"BMI: {bmi:.1f} - Normal weight")
elif bmi < 30:
    print(f"BMI: {bmi:.1f} - Overweight")
else:
    print(f"BMI: {bmi:.1f} - Obese")

# Output: BMI: 22.9 - Normal weight
```

### Example 10: Discount Calculator

```python
total_amount = 150
is_member = True

if is_member:
    if total_amount >= 100:
        discount = 0.20  # 20% discount
        print("Member discount: 20%")
    else:
        discount = 0.10  # 10% discount
        print("Member discount: 10%")
else:
    if total_amount >= 200:
        discount = 0.05  # 5% discount
        print("Non-member discount: 5%")
    else:
        discount = 0  # No discount
        print("No discount")

final_amount = total_amount * (1 - discount)
print(f"Final amount: ${final_amount:.2f}")

# Output:
# Member discount: 20%
# Final amount: $120.00
```

---

## Summary

Conditional statements (`if`, `elif`, `else`) enable programs to make decisions and execute different code based on conditions. The `if` statement tests a condition, `elif` provides additional conditions to test, and `else` handles all other cases. Proper indentation and syntax are critical for conditional statements to work correctly.

**Key Takeaways:**
- `if` tests conditions and executes code when `True`
- `elif` provides additional conditions (multiple allowed)
- `else` executes when all conditions are `False` (optional)
- Only one code block executes (first matching condition)
- Indentation defines code blocks (4 spaces or 1 tab)
- Colons (`:`) are required after each condition
- Conditions can be combined using logical operators (`and`, `or`, `not`)

---

## Quick Reference

### Basic Syntax
```python
# Simple if
if condition:
    statement

# if-else
if condition:
    statement
else:
    statement

# if-elif-else
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Common Patterns
```python
# Check range
if 0 <= score <= 100:
    print("Valid score")

# Multiple conditions
if age >= 18 and has_id:
    print("Access granted")

# Nested conditions
if condition1:
    if condition2:
        statement

# Checking membership
if item in list:
    print("Found")
```

---

## Review Questions

1. **What is the purpose of the `if` statement?**
   - Answer: To execute code only when a condition is `True`.

2. **What does `elif` stand for?**
   - Answer: "else if" - it tests additional conditions if previous conditions are `False`.

3. **Is the `else` block required in an `if` statement?**
   - Answer: No, it is optional.

4. **What happens if multiple conditions in an `if-elif-else` chain are `True`?**
   - Answer: Only the first `True` condition's code block is executed; the rest are skipped.

5. **What is the correct syntax: `else if` or `elif`?**
   - Answer: `elif`

6. **What character must appear at the end of `if`, `elif`, and `else` lines?**
   - Answer: A colon (`:`)

7. **How is the code block under an `if` statement defined?**
   - Answer: By indentation (typically 4 spaces or 1 tab).

8. **What is the output of the following code?**
   ```python
   x = 10
   if x > 5:
       print("A")
   elif x > 8:
       print("B")
   else:
       print("C")
   ```
   - Answer: `A` (first condition is `True`, so subsequent conditions are not checked)

9. **Can you have multiple `elif` blocks?**
   - Answer: Yes, you can have as many `elif` blocks as needed.

10. **Write an `if` statement to check if a number is positive.**
    - Answer: `if number > 0: print("Positive")`

---

## Further Study

**Related Topics:**
- Ternary conditional expressions (one-line conditionals)
- Match-case statements (Python 3.10+)
- Exception handling with try-except
- Loop control with break and continue

**Recommended Resources:**
- Python if...else - Programiz: https://www.programiz.com/python-programming/if-elif-else
- Python Conditions - W3Schools: https://www.w3schools.com/python/python_conditions.asp
- Conditional Statements - Real Python: https://realpython.com/python-conditional-statements/

**Next Steps:**
- Proceed to Lesson 8: Lists in Python
- Practice writing conditional statements with different scenarios
- Combine conditionals with user input and f-strings
- Build interactive programs that make decisions
