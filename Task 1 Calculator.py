'''Task 1 : Calculator
Create a basic calculator that can perform
basic arithmetic operations such as addition,
subtraction, multiplication, and division.using
functions'''
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0:
      return x / y
  else:
      return "Cannot divide by zero."

# Function to get user input and perform the calculation
def calculator():
  try:
      num1 = float(input("Enter the first number: "))
      operator = input("Enter the operator (+, -, *, /): ")
      num2 = float(input("Enter the second number: "))

      if operator == '+':
          result = add(num1, num2)
      elif operator == '-':
          result = subtract(num1, num2)
      elif operator == '*':
          result = multiply(num1, num2)
      elif operator == '/':
          result = divide(num1, num2)
      else:
          result = "Invalid operator. Please use +, -, *, /."

      print(f"Result: {result}")

  except ValueError:
      print("Invalid input. Please enter valid numbers.")

# Call the calculator function
calculator()
