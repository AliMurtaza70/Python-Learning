# Importing in Python
# -------------------
# Importing in Python is the process of loading code from a Python module
# into the current script. This allows you to use the functions and variables
# defined in the module, as well as any additional modules it may depend on.

# Basic import example:
# ---------------------
import math  # Imports the entire math module

# You can use functions and variables with dot notation:
result = math.sqrt(9)
print(result)  # Output: 3.0

# Using 'from' keyword:
# ---------------------
# You can import specific functions or variables from a module:
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0

# Importing multiple items:
from math import sqrt, pi
print(sqrt(9))  # Output: 3.0
print(pi)       # Output: 3.141592653589793

# Importing everything (not recommended):
# ---------------------------------------
# This can lead to confusion and naming conflicts:
from math import *
print(sqrt(9))  # Output: 3.0
print(pi)       # Output: 3.141592653589793

# Using 'as' keyword:
# -------------------
# This lets you rename a module when importing it:
import math as m
print(m.sqrt(9))  # Output: 3.0
print(m.pi)       # Output: 3.141592653589793

# Exploring module contents:
# ---------------------------
# Use the built-in dir() function to view all functions, variables, etc. in a module:
import math
print(dir(math))  # Lists all attributes of the math module

# Summary:
# --------
# - Use `import module` to load a full module.
# - Use `from module import name` to load specific items.
# - Use `from module import *` to import everything (not recommended).
# - Use `import module as alias` to rename a module.
# - Use `dir(module)` to inspect what's inside a module.
