# function for enhanced calculator
def calculator(first_number, second_number, op):
    if op == '+':
        result = add(first_number, second_number)
        print(result)
    elif op == '-':
        result = subtract(first_number, second_number)
        print(result)
    elif op == '*':
        result = multiply(first_number, second_number)
        print(result)
    elif op == '/':
        result = divide(first_number, second_number)
        print(result)
    else:
        print(f'Entered operator {op} is invalid!')


# function to add two numbers
def add(first_number, second_number):
    return first_number + second_number


# function to subtract two numbers
def subtract(first_number, second_number):
    return first_number - second_number


# function to multiply two numbers
def multiply(first_number, second_number):
    return first_number * second_number


# function to divide two numbers
def divide(first_number, second_number):
    return first_number / second_number


# main function for enhanced calculator
if __name__ == '__main__':
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    operator = input('Enter an operator: ')
    calculator(x, y, operator)
