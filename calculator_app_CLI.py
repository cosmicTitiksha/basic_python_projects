def calculation(operand1, operand2, operation):
  if operation == '+':
    print(f"So you want addition {operand1+operand2}")
  elif operation == '-':
    print(f"Okay subtraction {operand1-operand2}")
  elif operation == '*':
    print(f"Their product is {operand1*operand2}")
  elif operation == '/':
    if operand2 == 0:
      print("Sorry, can't be divided by 0, No definite answer!")
    else:
      print(f"The quotient is {operand1/operand2}")
  else:
    print(f"We are building this app for {operation} as well.")

while True:
    operand1 = float(input("Enter first number: "))
    operand2 = float(input("Enter second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    calculation(operand1, operand2, operation)

    iteration = input("Have more calculations to perform? (yes/no): ").lower()
    if iteration != 'yes':
        print("Okay, until next time!")

        break
