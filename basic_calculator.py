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


# main function for basic calculator
if __name__ == '__main__':
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    addition = add(x, y)
    print(addition)
    subtraction = subtract(x, y)
    print(subtraction)
    multiplication = multiply(x, y)
    print(multiplication)
    division = divide(x, y)
    print(division)
