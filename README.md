# Learning Basic Python 

#### Module 1:
- Interactive shell
```
$ python
Python 3.1.1 (r311:74483, Aug 17 2009, 17:02:12)
[GCC 4.2.3 (Debian 4.2.3-5)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
- Command Line Interface (CLI): CLI is used to execute commands from the terminal.
- Comments:
```
# Single-line comment

"""
Multiple-line 
comment
"""

'''
Multiple 
line 
comment
'''
```
- Indentation: Python works on indentation, and is an interpreted language.
- Execution: `$ python3 sample_file.py`
- Integrated Development Environment (IDE): IDE has all the features like terminal, code-editor and compiler in-built into it.
- Input: `name = input('Enter your first name: ')`
--------------
```
# Print statement
print("Lovish Arora")

# Drawing a shape
print('Printing a right angled triangle')
print("   /|")
print('  / |')
print(' /  |')
print('/___|')

# Variables and Data types
character_name = 'Lovish'
character_age = 28
is_male = True
print('There once was a man named ' + character_name + ', ')
print('he was ' + str(character_age) + ' years old.')
character_name = 'Ankush'
print('He really liked the name ' + character_name + ', ')
print("but didn't like being " + str(character_age) + ".")

# Working with Strings
print('Giraffe\nAcademy')       # new line character
print('Giraffe\"Academy')       # escape character/ sequence
print('Giraffe \\Academy')      # escape backslash
phrase = 'Giraffe Academy'
print(phrase + ' is cool.')     # string concatenation
print(phrase.lower())           # lower case characters
print(phrase.upper())           # upper case characters
print(phrase.islower())         # is in lower case
print(phrase.upper().isupper()) # is in upper case
print(len(phrase))              # length of phrase string
print(phrase[0])                # accessing character at a given index starts at 0
print(phrase[3])
print(phrase.index('A'))        # pass a parameter to function to identify its location
print(phrase.index('raffe'))
new_phrase = 'What a Giraffe Giraffe Giraffe!'
print(new_phrase.index('Giraffe'))  # prints first occurrence of the given substring
# print(new_phrase.index('Lovish'))   # ValueError: substring not found
print(new_phrase.replace('G', 'L')) # replace a character/ words in a phrase
print(new_phrase.replace('Giraffe', 'Elephant'))
```

--------
```
# Working with numbers
print(3)
print(3.5677)
print(-4.783329)
print(3 + 4.5)  # addition
print(3 - 4.5)  # subtraction
print(3 * 4.5)  # multiplication
print(3 / 4.5)  # division
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num) + ' my favourite number')
# print(my_num + ' my favourite number')  # Expected type 'int', got 'str' instead
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

my_num = -5.3
print(abs(my_num))  # absolute value function
print(pow(2, 3))  # power function
print(max(5, -4))  # max function
print(min(5, -4))  # min function
print(round(-3.4))  # round function
print(round(-3.8))

from math import *  # math module with lots of functions

print(floor(my_num))  # floor method
print(ceil(my_num))  # ceil method
print(sqrt(36))  # sqrt method

# Getting input from users
name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello ' + name + "! You are " + age + ' years old.')

# Building a basic calculator
num1 = input('Enter a number: ')  # by default string inputs
num2 = input('Enter another number: ')
result = float(num1) + float(num2)
print('result: ' + str(result))
```
-----------
```
# Mad Libs Game
color = input('Enter a color: ')
plural_noun = input('Enter a plural noun: ')
celebrity = input('Enter a celebrity name: ')
print('Roses are ' + color)
print(plural_noun + ' are blue')
print('I love ' + celebrity)

# Lists
friends = ['Mukul', 'Sarthak', 'Harshvardhan', 'Prateek', 'Yashika']
print(friends)
print(friends[1])
random_data = ['Lovish', 1996, 749.01, 'Sriganganagar', 'Yashika', 'Ankush']  # arbitrary data types
print(random_data[1])
print(random_data[-1])  # accessing from back - circular
print(random_data[1:])  # excluding start or end elements
print(random_data[2:5])  # accessing range
random_data[1] = 1995
print(random_data[1])

# List Functions
lucky_numbers = [42, 8, 15, 6, 231, 42]
print(lucky_numbers)
print(friends)
friends.extend(lucky_numbers)  # extends a list using another list
print(friends)
friends.append('Creed')  # appends an item to the end of the list
print(friends)
friends.insert(2, 'Mayank')  # add element at a given index
print(friends)
friends.remove('Sarthak')  # remove a specific element from the list
print(friends)
friends.pop()  # pop out last element
print(friends)
print(friends.index('Harshvardhan'))  # tells index of element, used for existence
# print(friends.index('Veenu'))   # ValueError: 'Veenu' is not in list
friends.append('Harshvardhan')
print(friends.count('Harshvardhan'))  # count of similar elements
lucky_numbers.sort()  # sorts a list
lucky_numbers.reverse()  # reverses a list
print(lucky_numbers)
new_lucky_numbers = lucky_numbers.copy()
print(new_lucky_numbers)
friends.clear()  # clears the whole list
print(friends)
```


