# String formatting in python
# String formatting can be done in python using the format method.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

# Example
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

# In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

# We can use it in a single statement as well.
# Example
print(f"{2 * 30}")



# Docstrings in python
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

# Example
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
# Here,
'''Takes in a number n, returns the square of n''' # is a docstring which will not appear in output

# Here is another example:

def add(num1, num2):
    """
    Add up two integer numbers.
    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.
    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.
    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.
    See Also
    --------
    subtract : Subtract one integer from another.
    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


# Python Comments vs Docstrings
# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the doc attribute.

# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

# Example
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)