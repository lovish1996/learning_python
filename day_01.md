#### Installing and using Python 3 Interpreter
- Check if python interpreter is already installed: `$ python3 --version` or `$ python3 -V` 
  - Output: `Python 3.11.1`
- If interpreter is not installed, download it for your OS from `www.python.org`
- In order to work with python interpreter, use: `$ python3`
```
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
- Python interpreter helps you to `execute python statements` one by one. Use `exit()` or `quit()` functions to exit python interpreter and return to OS prompt.
```
>>> 2+3
5
>>> 3*4
12
>>> 2**3
8
>>> exit()
$ 
```

#### IDLE and PyCharm (IDE)
- IDLE is python's integrated development environment(IDE) that comes with it's installation. It is color syntax-highlighting editor, has a debugger, Python shell, and python documentation set.
- When we start IDLE, we see triple chevron `>>>` prompt. IDLE is suitable for learning language syntax.
```
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
- We can also use PyCharm to write python code.
- Use `TAB` key for auto-completion in PyCharm. For example type `pr` and press `TAB` to call `print()` function.
- Navigating to previous and new commands
  - On Windows: `Alt+P` for previous and `Alt+N` for next statement.
  - On MAC: `Ctrl+P` for previous and `Ctrl+N` for next statement.
- Edit previous commands using `arrow keys` on keyboard even for multiple lines.

#### About Python
- Python language works with indentation. Unlike C/C++, where we use `{ and }` to define blocks, python uses `:` to define blocks along with indentation.
```
def method_name(parameter):
  # write method code here
```
- Comments: lines of code which are not executed.
  - Single-line comment: `# single-line comment`
  - Multi-line comment: Also known as documentation comment.
```
'''
This is multiple
line
comment
'''
```

#### Input-Output in PyCharm
- Create a new file by right-clicking on `your_project` in `PyCharm` `Project Structure/ Hierarchy`.
  - `Right click on your_project --> New --> Python File --> first.py`
- Enter the content [input_output.py](https://github.com/lovish1996/learning_python/blob/main/input_output.py)
- Run command `$ python3 input_output.py` to execute the contents of the file.





