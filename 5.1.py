#if statement
num: int = -10


if num < 0:
    print("The number is negative.")

    #if-else 
    num: int = -15

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

    #if-elif-
    num: int = 0

if num > 0: 
    print("The number is positive.")
elif num < 0: 
    print("The number is negative.")
else: 
    print("The number is zero.")


     
num: int = 5
#num: int = -10

if num > 0: # check wather the number is positive or negative

    if num % 2 == 0: # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else: # remainder 1 = odd_number,
        print("The number is positive and odd.")

else:
    print("The number is negative.")





    # Simple Calculator Program

# Taking user input
operation = input("Enter the operation (+, -, *, /): ").strip()
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."

except ValueError:
    result = "Error: Please enter valid numeric values."

# Displaying the result
print("Result:", result)


