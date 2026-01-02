# Project - create a calculator

def calculator( a, b, operation):
  if operation == "add":
    return a + b
  elif operation == "substract":
    return a - b
  elif operation == "multiply":
    return a * b
  elif operation == "divide":
    return a / b
  else:
    return "invalid operation"

print(calculator(34, 5, "add"))
print(calculator(34, 5, "substract"))
print(calculator(34, 5, "multiply"))
print(calculator(34, 5, "divide"))