number1 = int(input("Enter the first number: "))
operationSign = input("Enter the arithmetic operation (+, -, *, /): ")
number2 = int(input("Enter the second number: "))

if operationSign == '+':
    result = number1 + number2
elif operationSign == '-':
    result = number1 - number2
elif operationSign == '*':
    result = number1 * number2
elif operationSign == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operation!"

print(f"Result: {result}")