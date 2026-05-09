# Creating Virtual Environment

```bash
python -m venv myenv
```

# Module

*A module* is way that python provides in order to deal and use all the definations of some other program into the interactive instace of the interpreter. 

For example, `math` is a module which we can import in our script to use definations defined in `math`.

```python
import math as m

print(m.sin(90/2))
print(m.pi)
```

Here the `m` is an alias to the math module, that means all the defination are imported to the current running instance of interpreter and are callable only by the module name, using `math.sin` or `math.pi`, if you want to call them as if they are defined inside the running instace of the interpreter itself, then you need to `from math import sin, pi` to call them as they are defined within the script. *That's Python.*

*What does the random module do?* Generates pseudo-ramdom numbers. 

*What does the seed method of the random module do?* It is use to initialise the random number generation, 

*What is the difference between the randrange and randint methods?* `randint()` returns floating point and `randrange()` returns integer. And `randrange()` may take a step parameter

*What does the `random.seed()` do?* Output for the `random.random` will be same. 

*What will be the outcome of the `randrange(0,1)`*? It will be always zero, `randrange(0, 1)` function in Python's `random` module generates a random integer from the range `[0, 1)`, which means it includes the start value `0` but excludes the stop value `1`.

The `randrange(0, 1)` function in Python's `random` module generates a random integer from the range `[0, 1)`, which means it includes the start value `0` but excludes the stop value `1`.

Since there's only one possible value in this range (`0`), `randrange(0, 1)` will always return `0`.

If you want to generate a random integer that can be either `0` or `1`, you should use `randrange(0, 2)` or `random.randint(0, 1)`. This will give you a 50% chance of getting either `0` or `1`

*What does the `sample(teacher)` will return?* It will throw a `TypeError` because sample accepts two arguments. 

*What methods the python provide to print all the entities of the module?* `dir()` method 

When don't specify anything, `dir()` will print the current entities working in current interpreter instance along with all the entities imported. 

# Platform Module

Refer to [platform](https://docs.python.org/3/library/platform.html#module-platform) official docs from python.org to learn more about it. 

But to form an overview it gives all the platform level information about the instance on which you are running the code. 

```python
from platform import platform
from platform import machine
from platform import version
from platform import system
```

*If you would like to know which OS (Operating System) you are on:* Use `platform.system()`

*What is the difference between the platform's version and python_version functions?* `version()` returns the platform version, whereas `python_version()` returns the version of python current interpreter is using. 

*Which of the following code snippets may return 'CPython'?* `python_implementation()`

# Modules and Packages

We can also write our module and import it in other scripts to use the contents of the module that your imported. 

Module initialise only onces when it is imported within a script, when the script is run it will initialise the code of the module only once. 

When the code is run/imported, it depends whether the code is imported or run directly. The `__name__` variable that is initialised whenever the code is run, if the `__name__` is equal to `__main__` that means code is run directly the `__name__` attribute is set to `__main__` which helps us to detect in which context the code has been executed. 

> Remember when you initialise your module, python remembers which module is initialised so even if you want to imported a single module two times, it will be initialised only once. 

When you create a module of yourself, python searches for the module in path which you can identify using `sys.path` which store the location in which python searches for the modules. 

```python
import sys

for p in sys.path:
    print(p)
```

This is print out the directories to which python searches, if you created a directory and started importing your modules which in are not in `sys.path` directory, you will probably get an error. 

> Python is able to search through the zip files as well, so you can also create a zip folder and import all the modules from the zip folder, which is quite memory efficient. 

Use the `sys.append()` method to append the directory to the python search library. 

```python
from sys import path

path.append('ownModule')

form ownModule import module
```

You need to then specify while importing the module. 

```python
from ownModule.module import get_sum
```

*When a module is imported:..* All its entities are executed implicitly.

*The recommended method is to import just the module. Why?* 

The `__init__.py` file is a special file in Python that serves several purposes:

1. *Marks a directory as a package*: When a directory contains an `__init__.py` file, Python treats it as a package, allowing you to import modules from that directory.

2. *Initializes the package*: The `__init__.py` file can contain code that initializes the package, such as setting up package-level variables or importing modules.
3. *Specifies package metadata*: You can add metadata to the `__init__.py` file, such as the package's version, author, and description.

A typical `__init__.py` file might contain:
```python
# Specify package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Import modules to make them available at the package level
from .module1 import function1
from .module2 import function2

# Initialize package-level variables
package_variable = "some value"
The purpose of `__init__.py` is to:
```

- Make your package importable
- Provide a way to initialize the package
- Specify package metadata
- Make package-level imports and variables available

You can leave the `__init__.py` file empty if you don't need to initialize the package or specify metadata. However, it's still necessary to include the file to mark the directory as a package.

In Python 3.3 and later, you can also use *namespace packages*, which don't require an `__init__.py` file. However, this is a more advanced topic, and traditional packages with `__init__.py` files are still widely used.

# Python Package Installer

Pip stands for python install packages. These are third-party python packages which can be installed using internet via PyPI Repo, also called Python Package Installer. 

Use `pip list` to find all the pip installed packages on the local machine. 

*What `__pycache__`* is for? It install all the compiled python code. The pyc files has the compiled python code. 

*Did you know that the PyPI repo is also referred to as the Cheese Shop? The analogy comes from a British entertainment show by Monty Python, a comedy group. In one of their sketches, we watch a failed visit to a cheese shop where there is no cheese in the stock. The Python language was named after Monty Python, since it was developed with the aim to be fun to work with, thus the official documentation’s tutorials often refer to spam and eggs (a reference to a Monty Python sketch) instead of the standard foo and bar.*

Please keep in mind that while PyPI is a free place to fetch packages, you need to respect the licenses that come with the packages.

# Strings 

There are string methods which are some of the most used. 

```python
print(ord('L')) # 76

print(chr(76)) # L

# Access the string element
message='New York'
print(message[0])

# You can Slice the string
print(message[5:])
```

But remember that strings are immutable so you can't delete the elements from the string, you can't append elements to strings. 

```python
print(min('aghgGAghg')) # A
print(max('Hello World!')) # r

# Indexing in Strings
print('Hello world!'.index('w'))

# Counting in Strings
print('Hello world!'.count('o'))

# String as List
print(list('Hello World'))
```

Refer to [String Constants](https://docs.python.org/3/library/string.html#module-string) which are needed to import using the `import string`, thus, this means then you can access all the string constants like digits, ascii_lowercase, ascii_upercase.

*How many Latin characters are stored in String?* 128

Use `str.capitalize()` to capitalise the string in order to change the lowercase into uppercase, it doesn't modify the original string, but only the lowercase letters. 

Use `str.centre()` to pad the string with given charater. 

Use `str.endswith()` method to check if the sting ends with specified character. 

Use `str.startwith()` to check if string starts with specified character. 

The issue is that `rstrip('.shitthing')` removes all trailing characters that are in the string `'.shitthing'`, not the exact string `'.shitthing'`.

In your case, `rstrip('.shitthing')` is removing all trailing characters that are `.`, `s`, `h`, `i`, `t`, `n`, or `g`. That's why you're getting `wwww.some` instead of `wwww.something`.

If you want to remove the exact string `'.shitthing'`, you can use the `str.removesuffix()` method (Python 3.9+) or string slicing:

```python
print('wwww.something.shitthing'.removesuffix('.shitthing'))  # wwww.something

# or
s = 'wwww.something.shitthing'
print(s[:-len('.shitthing')] if s.endswith('.shitthing') else s)  # wwww.something
```

Alternatively, you can use string replacement:

```python
print('wwww.something.shitthing'.replace('.shitthing', ''))  # wwww.something
```

Use `str.lstrip`, `str.rstrip` and `str.strip` method to remove the leading, trailling, and both leading & trailling characters. 

Then you can use `str.replace` to replace the sting, `str.swapcase` to swap the cases of each character, then `str.title` for convert the string into a title format. 

> `\n` is considered a whitespace character.

# Interesting Case

```python
>>> chars='1234'
>>> char=''
>>> for char in reversed(chars):
...   char+=char
... 
>>> char
'11'
```

1. `chars = '1234'`: You assign the string `'1234'` to the variable `chars`.
2. `char = ''`: You assign an empty string to the variable `char`. This variable will be overwritten in the loop.
3. `for char in reversed(chars):`: You iterate over the characters in `chars` in reverse order (`'4'`, `'3'`, `'2'`, `'1'`). In each iteration, the variable `char` takes on the value of the current character.
4. `char += char`: Inside the loop, you're appending the current value of `char` to itself. This is where things get interesting.

Let's go through the iterations:

- `char = '4'`, `char += char` => `char = '44'`
- `char = '3'`, `char += char` => `char = '33'`
- `char = '2'`, `char += char` => `char = '22'`
- `char = '1'`, `char += char` => `char = '11'`

After the loop finishes, the value of `char` is `'11'`, which is the result of the last iteration.

The key point is that the `char` variable is reassigned in each iteration, so the previous value is lost. The `char += char` operation only affects the current value of `char`, and the result is overwritten in the next iteration.

If you want to accumulate the characters, you might want to use a different variable, like this:

```python
result = ''
for char in reversed(chars):
    result += char
print(result)  # Output: '4321'
```

# Exceptions

*What may happen if our Python program does not handle errors?* The program waits for problem handling, if not present, the program stop running and throws an error. 

*What mechanisms does Python provide to deal with errors?* Exeptional Raising, keyowrds like `try`, `except`. 

The `except` block only executes if the try block fails. 

*How many exceptions branches can we have in a try/except block?* More than one as long as the branch has the unique name

*Which one of the following is Unhandled Error?*

*What does the unnamed exception is?*

*What happens when an exception branch is executed?*

*Which of the following code snippets would raise an unhandled exception?*
```python
# A
try:
    x = y + 1
except NameError:
    print("y is not defined")
    x = y + 1

# B
try:
    x = 'seasalt'[7]
except IndexError:
    print("No character found in that index")

# C
try:
    x = 'y' + 1
except ValueError:
    print("y is not a number value")
```

Normally the code is as follows:

```python
A recap of the exception branches order:
try:
      #
      # Some code
      #
except ExceptName1:
      # Error handling related to Name1
except ExceptName2:
      # Error handling related to Name2
except:
      # Any other issues fall here

# Some more code
```



### **ZeroDivisionError**
Occurs when a number is divided by zero — mathematically undefined and not allowed.
```python
a = 10
b = 0
print(a / b)  # ZeroDivisionError: division by zero
```
This is common in finance or calculations where inputs aren’t validated.


### **AssertionError**
Triggered when an `assert` statement fails. Used for debugging or enforcing assumptions.
```python
age = -1
assert age >= 0, "Age must be non-negative"
```
Helpful in test-driven development or sanity-checking input.


### **IndentationError**
Occurs when code indentation is misaligned — Python uses indentation to define code blocks.
```python
def greet():
print("Hello")  # IndentationError: expected an indented block
```
This error typically happens due to poor formatting or mixing tabs/spaces.


### **ValueError**
Raised when a function receives an argument of the right type but inappropriate value.
```python
int("hello")  # ValueError: invalid literal for int()
```
Often encountered during type conversion or unpacking values.


### **AttributeError**
Occurs when an object doesn't have the attribute you're trying to access.
```python
s = 123
s.upper()  # AttributeError: 'int' object has no attribute 'upper'
```
Common mistake when confusing data types, like integers vs strings.


### **StopIteration**
This error is raised internally to signal the end of an iterator.
```python
it = iter([1, 2])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # StopIteration
```
Usually seen in custom iterators or when manually looping using `next()`.


### **TypeError**
Happens when an operation is performed on an object of inappropriate type.
```python
print("hello" + 5)  # TypeError: can only concatenate str (not "int") to str
```
Occurs often when combining types like str + int or using `*` between two strings.


### **IndexError**
Raised when trying to access an index that’s out of range.
```python
lst = [1, 2, 3]
print(lst[5])  # IndexError: list index out of range
```
Common in loops and algorithms when indexing beyond list bounds.


### **RuntimeError**
Generic error raised when something goes wrong that doesn't fall under other exceptions.
```python
def recursive():
    return recursive()
recursive()  # RuntimeError: maximum recursion depth exceeded
```
Useful when writing custom libraries or control flows.

### **SystemError**
This happens when the interpreter detects internal problems, generally very rare.
```python
import array
array.array('u')  # SystemError: bad argument to internal function (depends on Python version)
```
It suggests something unexpected happened at a deeper interpreter level.


### **KeyError**
Occurs when a dictionary is accessed with a key that doesn’t exist.
```python
data = {"name": "Alice"}
print(data["age"])  # KeyError: 'age'
```
This often arises in parsing JSON or dictionary operations without `get()`.

### **OverflowError**
Raised when a number exceeds the limit of a data type (usually in floating point operations).
```python
import math
print(math.exp(1000))  # OverflowError: math range error
```
Seen in scientific computing or recursive calculations.

### **TabError**
Raised when inconsistent use of tabs and spaces is found.
```python
def greet():
\tprint("Hi")  # Mixed tabs and spaces
    print("Hello")  # TabError
```
Happens often when copying code from the web or mixing editors.


### **ReferenceError**
Occurs when accessing a weak reference that has been garbage collected.
```python
import weakref

class Foo: pass
obj = Foo()
r = weakref.ref(obj)
del obj
print(r())  # ReferenceError: weakly-referenced object no longer exists
```
Used rarely unless working with memory management or caching mechanisms.

### **UnicodeError**

Occurs when encoding or decoding fails.
```python
b = "你好".encode('ascii')  # UnicodeEncodeError
```
Common when handling multilingual data in text files or databases.


# Understanding `try/except` blocks

Lets first see the first block which has `except` at the end. 

```python
def division():
    try:
        global number1, number2
        number1 = input("Enter a number: ")
        number2 = input("Enter another number: ")
        print(float(number1) / float(number2))
    except ZeroDivisionError:
        print("Zero division error, please try again.")
        division()
    except TypeError:
        print("Please enter valid numbers.")
        division()
    except:
        print("Hmm, something went wrong, try again.")
        division()
division()
```

In the first code snippet, the last block is an `except` block without specifying any particular exception type. This is known as a bare `except` clause, and it will catch any exception that is not caught by the previous `except` blocks. This can be useful for logging or handling unexpected errors, but it can also mask bugs in your code if not used carefully.

If the last block is an `else` block instead of `except` block,  the `else` block in a try-except statement is executed when the code in the `try` block does not raise any exceptions. This means that if the division operation is successful, the code in the `else` block will be executed.

# Hierarchy of Exceptions

Becuase every exception follows a hierarchy, it is possible to point out the exception right away. An exception `ZeroDivisionError` is case of `ArithmeticError`, similar to that 

A scenario where the `ArithmeticError` branch can catch multiple arithmetic errors, including `ZeroDivisionError`:

```python
try:
    x = 5 / 0
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")
```
In this case, the output would be:

```
An arithmetic error occurred: division by zero
```

`ArithmeticError` is a base class for several arithmetic-related exceptions, including:

- `ZeroDivisionError`: raised when you try to divide by zero.
- `FloatingPointError`: raised when a floating-point operation fails.
- `OverflowError`: raised when an arithmetic operation exceeds the limits of the numeric type.

By catching `ArithmeticError`, you can handle all these types of exceptions in a single block.

Here's another example that demonstrates multiple arithmetic errors:
```python
try:
    x = 5 / 0
except ArithmeticError as e:
    if isinstance(e, ZeroDivisionError):
        print("Cannot divide by zero!")
    elif isinstance(e, FloatingPointError):
        print("Floating-point operation failed!")
    else:
        print(f"An arithmetic error occurred: {e}")
```

In this case, if you try to divide by zero, it will print "Cannot divide by zero!". If you encounter another arithmetic error, it will print a corresponding message.

You can also have multiple `except` blocks to handle different types of exceptions:

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except FloatingPointError:
    print("Floating-point operation failed!")
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")
```

This way, you can handle specific exceptions differently while still having a catch-all for other arithmetic errors.

# Branching in Exception: Becuase Order Matters

Here's an example that demonstrates how the order of branching matters when writing try/except blocks:

```python
try:
    x = 5 / 0
except Exception as e:
    print("Caught a general exception")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

In this case, the output would be:
```
Caught a general exception
```
The reason for this is that the `except` blocks are evaluated in the order they appear in the code. Since `ZeroDivisionError` is a subclass of `Exception`, the first `except` block catches the exception and the second `except` block is never reached.

To fix this, you should put the more specific exception (`ZeroDivisionError`) before the more general exception (`Exception`):
```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Caught a general exception")

```

In this case, the output would be:
```
Cannot divide by zero!
```

This way, the more specific exception is caught and handled correctly, and the general exception block serves as a catch-all for any other unexpected exceptions.

This ordering rule applies to all exception hierarchies, not just `Exception` and its subclasses. For example, if you're catching both `ArithmeticError` and `ZeroDivisionError`, you should put `ZeroDivisionError` after `ArithmeticError` if you want to handle `ArithmeticError` more generally:

```python
try:
    x = 5 / 0
except ArithmeticError:
    print("An arithmetic error occurred")
except ZeroDivisionError:
    # This block will never be reached
    print("Cannot divide by zero!")
Instead, you should swap the order:
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ArithmeticError:
    print("An arithmetic error occurred")
```

# `raise` an Exception

A exception can be raise using `raise` keyword within one function and let another function deal with the error for better error handling:

```python
def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)

def main():
    try:
        numbers = []
        average = calculate_average(numbers)
        print(f"Average: {average}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
In this example:

- The `calculate_average` function raises a `ValueError` if the input list is empty.
- The `main` function calls `calculate_average` and catches the `ValueError` exception if it's raised.
- The `main` function handles the error by printing an error message.

This approach is beneficial for several reasons:

- *Separation of concerns*: The `calculate_average` function focuses on calculating the average, while the `main` function focuses on handling errors.
- *Reusability*: The `calculate_average` function can be reused in other parts of the code without worrying about error handling.
- *Better error handling*: The `main` function can handle errors in a way that's specific to the application's needs.

By raising exceptions in the `calculate_average` function and catching them in the `main` function, you can write more robust and maintainable code.

You can also add more specific error handling in the `main` function, such as:
```python
def main():
    try:
        numbers = []
        average = calculate_average(numbers)
        print(f"Average: {average}")
    except ValueError as e:
        if str(e) == "Cannot calculate average of an empty list":
            print("Please provide a non-empty list of numbers")
        else:
            print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
This way, you can handle specific errors differently and provide more informative error messages.

# Error Handling using `assert`

`assert` is not just a boolean function; it's a statement that lets you validate assumptions about your code. When an `assert` statement fails, it raises an `AssertionError`.


```python
# Assert statement
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# Equivalent if statement with raise
def divide(a, b):
    if b == 0:
        raise AssertionError("Cannot divide by zero")
    return a / b
```

The key difference between `assert` and an `if` statement is that `assert` statements can be disabled by running Python with the `-O` flag, which optimizes the code and removes `assert` statements. This makes `assert` suitable for debugging purposes.

In contrast, `if` statements are always executed and are used for control flow and error handling.
```python
# Running with -O flag disables assert statements
# python -O script.py
def divide(a, b):
    assert b != 0, "Cannot divide by zero"  # This line is ignored when running with -O
    return a / b
```

When to use `assert`:

```python
def calculate_area(width, height):
    assert width > 0 and height > 0, "Width and height must be positive"
    return width * height
```

When to use `if` for error handling:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

*What are the abstract exceptions?* It is the class of multiple types of exception that can be denoted as `Exception`

*Why shouldn't we put more general exceptions before specific ones?* The question is asking why you shouldn't put more general exceptions (like `Exception`) before specific ones (like `ZeroDivisionError` or `TypeError`).

```
try:
    x = 5 / 0
except Exception as e:
    print("Caught a general exception")
except ZeroDivisionError:
    print("Caught a ZeroDivisionError")
```

In this case, the `except Exception as e:` block will catch the `ZeroDivisionError` exception, because `ZeroDivisionError` is a subclass of `Exception`. The `except ZeroDivisionError:` block will never be reached.

# `BaseException` Class

The `BaseException` class in Python, which is the base class for all built-in exceptions. Here's a breakdown of the key points:

1. *Base class for all exceptions*: `BaseException` is the root of the exception hierarchy in Python. All built-in exceptions, such as `Exception`, `SystemExit`, `KeyboardInterrupt`, and others, inherit from `BaseException`.

2. *Not meant for direct inheritance*: While you can technically inherit from `BaseException` directly, it's not recommended. Instead, you should inherit from `Exception` or one of its subclasses. This is because `BaseException` includes exceptions that are typically used for system-level events, such as `SystemExit` and `KeyboardInterrupt`, which you might not want to catch in your code.

3. *`args` attribute*: When an exception is raised, it can take one or more arguments. These arguments are stored in the `args` attribute of the exception instance. Some built-in exceptions, like `OSError`, expect a specific number of arguments and assign special meanings to them.

4. *`with_traceback(tb)` method*: This method allows you to set a new traceback for an exception instance. It's useful when you want to preserve the original traceback of an exception while re-raising it as a different type of exception.

5. *`__traceback__` attribute*: This attribute holds the traceback object associated with the exception. You can access and modify it using the `with_traceback()` method.

6. *`add_note(note)` method and `__notes__` attribute*: These were added in Python 3.11 and allow you to add notes to an exception. These notes appear in the standard traceback after the exception string. You can add multiple notes to an exception, and they'll be stored in the `__notes__` attribute.

Here's an example of using some of these features:
```python
try:
    raise ValueError("Invalid value")
except ValueError as e:
    e.add_note("Please check your input")
    raise

# Output:
# ValueError: Invalid value
# Please check your input
```
And here's an example of using `with_traceback()`:

```python
import sys

try:
    raise ValueError("Invalid value")
except ValueError as e:
    tb = sys.exc_info()[2]
    raise RuntimeError("Something went wrong").with_traceback(tb)
```

*What is common between AssertionError and ArithmeticError?*
Both `AssertionError` and `ArithmeticError` are exceptions in Python.

The commonality between them is that they both inherit from the `Exception` class, which in turn inherits from the `BaseException` class.

In other words, both `AssertionError` and `ArithmeticError` are subclasses of `Exception`, which makes them part of the standard exception hierarchy in Python.

Here's the hierarchy:

- `BaseException`
    - `Exception`
        - `AssertionError`
        - `ArithmeticError`
            - `FloatingPointError`
            - `OverflowError`
            - `ZeroDivisionError`

This means that both `AssertionError` and `ArithmeticError` can be caught and handled using `try-except` blocks, just like other exceptions in Python.

# Multiple Errors

No, the syntax you're using is not valid for catching multiple exceptions in Python.

The correct syntax would be:
```python
except (TypeError, ZeroDivisionError):
    print("Please enter valid numbers, besides 0.")
```

This will catch both `TypeError` and `ZeroDivisionError` exceptions and trigger the `except` block if either of them occurs.

In your original code, the syntax `except TypeError, ZeroDivisionError:` is actually using a feature of Python 2.x where the comma is used to assign the exception instance to a variable. However, in this case, it's not doing what you intend it to do.

In Python 3.x, this syntax would raise a `SyntaxError`. The correct way to catch multiple exceptions is to use a tuple of exception types, as shown above.

So, to answer your question, if you use the correct syntax, the `except` block will trigger if either `TypeError` or `ZeroDivisionError` occurs, not just if both occur simultaneously.

# `Exception` Class

In this case if the `assert` is raising a error `AssertionError`, would that except `Exception` block be triggered?
```
def captcha():
    try:
        inp = int(input("3 + 16? "))
        assert inp == 19, "Wrong input, please try again."
    except Exception:
        print("Hmm, something went wrong, please try again.")
        captcha()


captcha()
```

Yes, the `except Exception` block would be triggered if the `assert` statement raises an `AssertionError`.

Here's why:

- `AssertionError` is a subclass of `Exception`
- The `except Exception` block catches all exceptions that are instances of `Exception` or its subclasses

Since `AssertionError` is a subclass of `Exception`, the `except Exception` block will catch the `AssertionError` raised by the `assert` statement.

So, in your code, if the user enters an incorrect answer, the `assert` statement will raise an `AssertionError`, which will be caught by the `except Exception` block, and the message "Hmm, something went wrong, please try again." will be printed.

It's worth noting that the `except Exception` block is quite broad, and it will catch many other types of exceptions besides `AssertionError`. If you want to handle `AssertionError` specifically, you could add a separate `except` block for it:
```python
def captcha():
    try:
        inp = int(input("3 + 16? "))
        assert inp == 19, "Wrong input, please try again."
    except AssertionError:
        print("Wrong input, please try again.")
    except Exception:
        print("Hmm, something went wrong, please try again.")
```
This way, you can provide a more specific error message for `AssertionError` cases.


# Object Oriented Programming v/s Procedural Programming

In object-oriented programming, inheritance allows one class to inherit properties and behavior from another class. When a subclass inherits from a parent class, it automatically takes on all the attributes and methods of the parent class. However, the subclass can also define its own attributes and methods or override the ones inherited from the parent class.

In the context of constructors, when a subclass defines its own constructor, it is responsible for calling the parent class constructor using the parent class name or the `super()` function. If the parent class constructor requires parameters, the subclass constructor must provide them when calling the parent class constructor.

Let's analyze the *code* and *output*:

*Class Hierarchy*

Refer to [code](/Users/utkarshsingh/Documents/learning-concepts/python/code/class_objects.py). You have two classes: `stack` and `addingStack`. `addingStack` inherits from `stack`.

*Constructors*

1. `stack` class:
    - `__init__` method is the constructor, which initializes an empty stack (`self.__stack = []`).
    - Prints "I am a constructor function!!" when an instance is created.
2. `addingStack` class:
    - `__init__` method is the constructor, which initializes the sum (`self.__sum = 0`) and calls the `stack` class constructor using `stack.__init__(self)`.
    - Prints "This is addStack constructor function!!" when an instance is created.

*Method Overriding*

`addingStack` class overrides two methods from `stack` class:

1. `push`: In `addingStack`, `push` method adds the value to the sum (`self.__sum += val`) and then calls the `push` method from `stack` class using `stack.push(self, val)`.
2. `pull`: In `addingStack`, `pull` method subtracts the pulled value from the sum (`self.__sum -= var`) and then returns the pulled value.

Method overriding is another key concept in object-oriented programming. When a subclass provides a different implementation of a method that is already defined in its parent class, it is said to override that method. The subclass method has the same name, return type, and parameter list as the parent class method, but it can have a different implementation.

*Output Analysis*

The output is consistent with the code's behavior, demonstrating inheritance, method overriding, and constructor chaining in Python.

1. When `stackObject` is created, the `stack` constructor is called, printing "I am a constructor function!!".
2. When `addStackObject` is created, the `addingStack` constructor is called, printing "This is addStack constructor function!!". The `addingStack` constructor then calls the `stack` constructor, printing "I am a constructor function!!".
3. Values are pushed and pulled from both `stackObject` and `addStackObject`. The sum is calculated and updated correctly in `addStackObject`.
4. The final output shows the sum of values in `addStackObject` before and after pulling a value, and the pulled value from `stackObject`.


In the example we saw earlier, the `addingStack` class inherits from the `stack` class and overrides the push and pull methods. The `addingStack` class also defines its own constructor, which calls the `stack` class constructor to initialize the stack. The push method in `addingStack` adds the value to the sum and then calls the push method in stack to add the value to the stack. Similarly, the pull method in `addingStack` subtracts the pulled value from the sum and then calls the pull method in stack to remove the value from the stack.

This design allows the `addingStack` class to build upon the functionality of the stack class while adding its own specific behavior. The use of inheritance and method overriding enables code reuse and facilitates the creation of a hierarchy of related classes that can be used to solve complex problems. By leveraging these object-oriented programming concepts, developers can write more efficient, modular, and maintainable code.

*What is the difference between procedural and Object-Oriented Programming (OOP)?* 

*What keyword do you use to define objects?* `class` keyword. 

*What is superclass in python?* A superclass in Python is a class from which another class inherits properties and behavior, providing a set of attributes and methods that can be used and built upon by its subclasses.

*Why this is correct*? An object has a name, property, and methods, and an object is an instance of a class. 

*Remember*:

The `__init__` method in Python is a special method that's automatically called when an object of the class is instantiated. It's used to initialize the attributes of the class.

However, `__init__` shouldn't return a value (other than `None`). When you try to return `self.para`, you'll get an error because `__init__` doesn't support returning values.

