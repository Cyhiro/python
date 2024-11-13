name = input('Please enter your name: ')
print('Hello ' + name + ', are you ready to do some simple math!')

# Get two numbers from the user
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

# Ask for the desired operation
operation = input('Enter a mathematical operation (+, -, *, /): ')

# Perform the operation based on user input and display the result
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Undefined (cannot divide by zero)'
else:
    result = 'Invalid operation'

print('Your answer is: ' + str(result))
