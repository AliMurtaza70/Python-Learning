# dir(), __dict__, and help() in Python
# In Python, there are three built-in tools commonly used to inspect objects and understand how classes and functions behave:

# dir()

# __dict__

# help()

# These are especially helpful for introspection—examining the type or properties of objects at runtime.

# 🔍 dir() Function
# The dir() function returns a list of all attributes and methods (including magic methods, also known as "dunder" methods) associated with an object.

# Example:
# python
# Copy
# Edit
# x = [1, 2, 3]
# print(dir(x))
# Output (partial):
# python
# Copy
# Edit
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
#  'pop', 'remove', 'reverse', 'sort']
# ✅ Use case: Discover what methods and properties are available on an object.

# 📦 __dict__ Attribute
# The __dict__ attribute returns a dictionary of all the instance variables (attributes) of an object.

# Example:
# python
# Copy
# Edit
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("John", 30)
# print(p.__dict__)
# Output:
# python
# Copy
# Edit
# {'name': 'John', 'age': 30}
# ✅ Use case: Access or modify the internal state (attributes) of an object dynamically.

# 📘 help() Function
# The help() function displays the documentation for an object, including available methods and their descriptions.

# Example:
# python
# Copy
# Edit
# help(str)
# Output (truncated):
# vbnet
# Copy
# Edit
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object...
# ✅ Use case: Explore detailed documentation and method signatures for built-in types or your custom classes.

# ✅ Conclusion
# The dir(), __dict__, and help() tools are powerful for:

# Exploring objects and their capabilities

# Debugging and understanding code

# Dynamically inspecting and modifying object states

# These are essential for learning, debugging, and building smarter programs using Python.

