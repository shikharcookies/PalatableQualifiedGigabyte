expression = input("Enter the expression in the form 'operand1 operator operand2': ")
operands = expression.split()  # Split the string into a list of operands and operator

operand1 = float(operands[0])
operand2 = float(operands[2])
operator = operands[1]

if operator == "+":
    result = operand1 + operand2
elif operator == "-":
    result = operand1 - operand2
elif operator == "*":
    result = operand1 * operand2
elif operator == "/":
    result = operand1 / operand2
else:
    print("Invalid operator. Please enter a valid operator (+, -, *, /).")
    exit()

print(f"{expression} = {result}")