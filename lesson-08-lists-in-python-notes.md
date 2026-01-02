# Lesson 8: Lists in Python

## Overview

Lists are one of the most versatile and commonly used data structures in Python. They allow you to store multiple items in a single variable, maintain order, and perform various operations on the collection. Understanding lists is fundamental to effective Python programming.

**Learning Objectives:**
- Understand what lists are and why they are useful
- Learn how to create and access list elements
- Master common list operations and methods
- Practice manipulating lists to solve problems

---

## Video Tutorial

Watch the video lesson for this topic:

<iframe width="560" height="315" src="https://www.youtube.com/embed/hK7ahe5EKV8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Direct Link:** [Watch on YouTube](https://youtu.be/hK7ahe5EKV8)

---

## Key Concepts

### What is a List?

A **list** is an ordered collection of items that can store multiple values in a single variable. Lists are:
- **Ordered**: Items maintain their position
- **Mutable**: Items can be changed after creation
- **Allow duplicates**: Same value can appear multiple times
- **Mixed types**: Can contain different data types

### Creating Lists

Lists are created using square brackets `[]` with items separated by commas.

**Syntax:**
```python
list_name = [item1, item2, item3]
```

### List Indexing

Each item in a list has an **index** (position number):
- First item: index `0`
- Second item: index `1`
- Last item: index `-1`
- Second-to-last: index `-2`

---

## Detailed Explanations

### 1. Creating Lists

**Empty List:**
```python
empty_list = []
```

**List with Items:**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
```

### 2. Accessing List Elements

Use the index in square brackets to access items:

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # First item: "apple"
print(fruits[1])   # Second item: "banana"
print(fruits[-1])  # Last item: "cherry"
```

### 3. Common List Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Access item | `list[index]` | Get item at index |
| Change item | `list[index] = value` | Modify item |
| Add item (end) | `list.append(item)` | Add to end |
| Add item (position) | `list.insert(index, item)` | Insert at position |
| Remove item | `list.remove(item)` | Remove first occurrence |
| Remove by index | `list.pop(index)` | Remove and return item |
| Length | `len(list)` | Number of items |
| Check membership | `item in list` | Check if item exists |

### 4. List Slicing

Extract portions of a list using slicing:

**Syntax:**
```python
list[start:end]      # Items from start to end-1
list[start:]         # Items from start to end
list[:end]           # Items from beginning to end-1
list[start:end:step] # With step
```

### 5. Essential List Methods

| Method | Description | Example |
|--------|-------------|---------|
| `append(item)` | Add item to end | `list.append(5)` |
| `insert(index, item)` | Insert at position | `list.insert(0, "first")` |
| `remove(item)` | Remove first occurrence | `list.remove("apple")` |
| `pop(index)` | Remove and return item | `list.pop()` or `list.pop(0)` |
| `clear()` | Remove all items | `list.clear()` |
| `sort()` | Sort in place | `list.sort()` |
| `reverse()` | Reverse in place | `list.reverse()` |
| `count(item)` | Count occurrences | `list.count(5)` |
| `index(item)` | Find first index | `list.index("banana")` |

---

## Important Points to Remember

- **Indexing starts at 0**: First item is `list[0]`, not `list[1]`
- **Negative indexing**: `-1` refers to the last item
- **Lists are mutable**: You can change, add, or remove items
- **IndexError**: Accessing an index that doesn't exist causes an error
- **`append()` vs `insert()`**: `append()` adds to end, `insert()` adds at specific position
- **`remove()` vs `pop()`**: `remove()` deletes by value, `pop()` deletes by index

**Common Mistakes to Avoid:**
- Using parentheses `()` instead of square brackets `[]`
- Forgetting that indexing starts at 0
- Trying to access an index that doesn't exist
- Confusing `append()` (adds one item) with `extend()` (adds multiple items)
- Modifying a list while iterating over it

---

## Practical Examples

### Example 1: Creating and Accessing Lists

```python
# Creating lists
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

# Accessing items
print(numbers[0])      # Output: 10
print(numbers[2])      # Output: 30
print(numbers[-1])     # Output: 50
print(fruits[1])       # Output: banana
```

### Example 2: Modifying List Items

```python
# Changing items
colors = ["red", "green", "blue"]
print(colors)          # Output: ['red', 'green', 'blue']

colors[1] = "yellow"   # Change second item
print(colors)          # Output: ['red', 'yellow', 'blue']
```

### Example 3: Adding Items to a List

```python
# Using append()
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Using insert()
fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
```

### Example 4: Removing Items from a List

```python
# Using remove() - removes by value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

# Using pop() - removes by index
numbers = [10, 20, 30, 40]
removed = numbers.pop(1)  # Remove index 1
print(numbers)            # Output: [10, 30, 40]
print(removed)            # Output: 20

# pop() without argument removes last item
last = numbers.pop()
print(numbers)            # Output: [10, 30]
print(last)               # Output: 40
```

### Example 5: List Length and Membership

```python
# Finding length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

# Checking membership
print("apple" in fruits)     # Output: True
print("grape" in fruits)     # Output: False
print("grape" not in fruits) # Output: True
```

### Example 6: List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # Output: [2, 3, 4] (index 2 to 4)
print(numbers[:4])     # Output: [0, 1, 2, 3] (start to 3)
print(numbers[5:])     # Output: [5, 6, 7, 8, 9] (5 to end)
print(numbers[-3:])    # Output: [7, 8, 9] (last 3)
print(numbers[::2])    # Output: [0, 2, 4, 6, 8] (every 2nd)
```

### Example 7: Sorting and Reversing

```python
# Sorting
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]

# Sorting in reverse
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 8, 5, 2, 1]

# Reversing
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']
```

### Example 8: Counting and Finding

```python
# Counting occurrences
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # Output: 3

# Finding index
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1
```

### Example 9: Iterating Through Lists

```python
# Using for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# With index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Example 10: Practical Use Case - Shopping List

```python
# Shopping list manager
shopping_list = []

# Adding items
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.insert(1, "butter")

print("Shopping List:")
for index, item in enumerate(shopping_list, 1):
    print(f"{index}. {item}")

# Output:
# Shopping List:
# 1. milk
# 2. butter
# 3. bread
# 4. eggs

# Remove item
shopping_list.remove("bread")
print(f"\nUpdated list: {shopping_list}")
# Output: Updated list: ['milk', 'butter', 'eggs']

# Check if item exists
if "milk" in shopping_list:
    print("Don't forget to buy milk!")
# Output: Don't forget to buy milk!
```

### Example 11: Working with Numbers - Statistics

```python
# Calculate basic statistics
scores = [85, 92, 78, 90, 88]

# Total and average
total = sum(scores)
average = total / len(scores)

print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

# Output:
# Scores: [85, 92, 78, 90, 88]
# Total: 433
# Average: 86.6
# Highest: 92
# Lowest: 78
```

---

## Summary

Lists are ordered, mutable collections that store multiple items in a single variable. They support indexing, slicing, and various operations for adding, removing, and modifying items. Lists are fundamental to Python programming and are used extensively for storing and manipulating collections of data.

**Key Takeaways:**
- Lists are created using square brackets: `[item1, item2, item3]`
- Indexing starts at 0; negative indexing starts from the end
- Lists are mutable (can be changed after creation)
- Common methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`
- Use `len()` to get list length
- Use `in` to check membership
- Slicing extracts portions: `list[start:end]`
- Lists can contain mixed data types

---

## Quick Reference

### Creating Lists
```python
empty = []
numbers = [1, 2, 3]
mixed = [1, "text", 3.14, True]
```

### Accessing and Modifying
```python
item = list[0]          # Access first item
list[0] = value         # Modify item
last = list[-1]         # Access last item
```

### Common Operations
```python
list.append(item)       # Add to end
list.insert(i, item)    # Insert at index
list.remove(item)       # Remove by value
item = list.pop(i)      # Remove by index
len(list)               # Get length
item in list            # Check membership
```

### Slicing
```python
list[2:5]               # Items 2 to 4
list[:3]                # First 3 items
list[3:]                # From index 3 to end
list[-2:]               # Last 2 items
list[::2]               # Every 2nd item
```

### Other Methods
```python
list.sort()             # Sort in place
list.reverse()          # Reverse in place
list.count(item)        # Count occurrences
list.index(item)        # Find index
list.clear()            # Remove all items
```

---

## Review Questions

1. **How do you create an empty list?**
   - Answer: `empty_list = []`

2. **What is the index of the first item in a list?**
   - Answer: `0`

3. **How do you access the last item in a list?**
   - Answer: `list[-1]`

4. **What is the difference between `append()` and `insert()`?**
   - Answer: `append()` adds an item to the end, while `insert()` adds an item at a specific index.

5. **How do you remove an item by value from a list?**
   - Answer: `list.remove(value)`

6. **What does `pop()` return?**
   - Answer: The removed item.

7. **How do you get the number of items in a list?**
   - Answer: `len(list)`

8. **What does `list[1:4]` return?**
   - Answer: Items at indices 1, 2, and 3 (not including index 4).

9. **How do you check if an item exists in a list?**
   - Answer: `item in list`

10. **Are lists mutable or immutable?**
    - Answer: Mutable (can be changed after creation).

---

## Further Study

**Related Topics:**
- List comprehensions (advanced list creation)
- Tuples (immutable lists)
- Nested lists (lists within lists)
- Looping through lists with `for` and `while`
- Copying lists (`copy()` vs `=`)

**Recommended Resources:**
- Python Lists - Official Docs: https://docs.python.org/3/tutorial/datastructures.html
- Python Lists - W3Schools: https://www.w3schools.com/python/python_lists.asp
- Python Lists - Programiz: https://www.programiz.com/python-programming/list
- Lists Tutorial - GeeksforGeeks: https://www.geeksforgeeks.org/python-lists/

**Next Steps:**
- Proceed to Lesson 9: Functions in Python - def and return
- Practice creating and manipulating lists
- Experiment with list methods and slicing
- Build programs that use lists to store and process data
