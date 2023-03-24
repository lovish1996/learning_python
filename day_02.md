#### PyCharm short-cuts
- Use `TAB` key for auto-completion.
- Use `option + command + L` for correcting indentation on `MAC` and `alt + ctrl + L` on `Windows`.

#### Data types Python V/s C++
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
- In Python, we use combinations of `if`, `elif` and `else` to make a ladder of nested if-else statements or simulate switch statements.
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
  
