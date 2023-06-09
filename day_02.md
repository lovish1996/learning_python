#### PyCharm short-cuts
- Use `TAB` key for auto-completion.
- Use `option + command + L` for correcting indentation on `MAC` and `alt + ctrl + L` on `Windows`.

#### Data types Python V/s C++
Refer [data_types.py](https://github.com/lovish1996/learning_python/blob/main/data_types.py) for more sample definitions.
- **integer**: `x = 10` V/s `int x = 10;`
- **float**: `x = 10.2345` V/s `float y = 10.2345;`
- **double**: Python does not have double V/s `double x = 2019.1526;`
- **boolean**: `x = True` V/s `bool x = true;`. Only two valid values `True/ False`.
- **character**: `x = 'a'` V/s `char x = 'a';`
- **string**: `x = 'sample'` V/s `string x = "sample";`

#### Method definitions Python V/s C++
- In Python, we use `:` to define a block of code in a method.
```
def method_name(parameter_1, parameter_2):
  y = 10
  first_statement
  second_statement
  third_statement
  return y
```
- In C++ we use `{ and }` to define a block of code in a method.
```
int method_name(parameter_1, parameter_2){
  y = 10;
  first_statement;
  second_statement;
  third_statement;
  return y;
}
```

#### If-else and nested if-else in Python V/s C++
- In Python, we use combinations of `if`, `elif` and `else` to make a ladder of nested if-else statements or simulate switch statements. Refer [if_else.py](https://github.com/lovish1996/learning_python/blob/main/if_else.py) for more details.
```
x = int(input('Enter an integer:'))
if x > 1:
  print('{x} is greater than 1.')
elif x < 1:
  print('{x} is less than 1.')
else:
  print('{x} is equals to 1.')
```
- Switch statement in Python:
```
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"
```
- In C++, we have if `if`, `else if` and `else` blocks for simulating if-else and `switch` statement for checking a set of values of a given variable.
```
int x;
cin >> x;
if (x > 1){
  cout << x << " is greater than 1." << endl;
} else if(x < 1){
  cout << x << " is less than 1." << endl;
} else{
  cout << x << " is equals to 1." << endl;
}
```
- Switch statement in C++:
```
string lang;
cin >> lang;
switch(lang){
  case "JavaScript":
    cout << "You can become a web developer.";
    break;
  case "PHP":
    cout << "You can become a web developer.";
    break;
  case "Python":
    cout << "You can become a Data Scientist";
    break;
  case "Solidity":
    cout << "You can become a Blockchain developer.";
    break;
  case "Java":
    cout << "You can become a mobile app developer";
    break;
  default:
    cout << "Invalid input!";
}
```
  
#### Boolean expressions and short-circuit
- `and`:
  - True and True = True
  - True and False = False
  - False and True = False    `1 > 3 and 2 < 4 = False because 1 < 3 will never check 2 < 4`
  - False and False = False   `1 > 3 and 2 > 4 = False because 1 < 3 will never check 2 > 4`
- `or`:
  - True or True = True       `1 < 3 or 2 < 4 = True because 1 < 3 will never check 2 < 4`
  - True or False = True      `1 < 3 or 2 > 4 = True because 1 < 3 will never check 2 > 4`
  - False or True = True
  - False or False = False 
- `not`:
  - not (1 > 3) = True
  - not (1 < 3) =  False

#### For Loop
- Refer [for_loop.py](https://github.com/lovish1996/learning_python/blob/main/for_loop.py) for sample definitions.
- Range function is useful for incrementing index variable `range()`. It has various implementations for different use cases.
- `range(10): 0 .. 9`
```
def for_loop():
    for i in range(10):  # i 0 .. 9        0 included 10 excluded
        print(i)
```
- `range(3, 11): 3 .. 10`
```
def for_loop_start():
    for i in range(3, 11):  # i 3..10       3 included 11 excluded increment 1
        print(i)
```
- `range(3, 11, 2): 3 5 7 9`
```
def for_loop_increment():
    for i in range(3, 11, 2):  # i 3 5 7 9       3 included 11 excluded increment 2
        print(i)
```
- `range(11, 3, -2): 11 9 7 5`
```
def for_loop_decrement():
    for i in range(11, 3, -2):  # i 11 9 7 5       11 included 3 excluded decrement 2
        print(i)
```

#### While Loop
- Refer [while_loop.py](https://github.com/lovish1996/learning_python/blob/main/while_loop.py) for sample definitions.
```
def while_loop():
    i = 5
    while i >= 0:
        print(i)  # 5 4 3 2 1 0
        i -= 1
```

#### Exercises:
1. Write a program to accept percentage from the user and display the grade according to the following criteria: [Solution](https://github.com/lovish1996/learning_python/blob/main/percentage_grade.py)
  - Marks > 90 : `Grade A`
  - Marks > 80 and <= 90: `Grade B`
  - Marks >= 60 and <= 80: `Grade C`
  - Below 60: `Grade D`
2. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for `Sunday`, 2 for `Monday` and so on. [Solution](https://github.com/lovish1996/learning_python/blob/main/weekday.py)
3. Print sum of all even numbers from 10 to 20 using for loop. [Solution](https://github.com/lovish1996/learning_python/blob/main/sum_10_to_20.py)
4. Calculate the square of all the odd numbers from 1 to 11 and print them. [Solution](https://github.com/lovish1996/learning_python/blob/main/calculate_squares.py)
5. Check how many times a given number can be divided by 3 before it is less than or equal to 10. [Solution](https://github.com/lovish1996/learning_python/blob/main/division_by_3.py)
