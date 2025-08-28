#In python we declare varibales directly not like js in var, let or const.
a=10
print(a)

# To check the type of a we use type()
print("The type of a is", type(a))

# Data type in Python.
b = "Hello I'm Aly"
c = None
# there are two other of number below you can see   
d = complex(2, 3)
e = 2.5
print("The type of a is", type(b))
print("The type of a is", type(c))
print("The type of a is", type(d))
print("The type of a is", type(e))


# In Python, lists and tuples are both used to store collections of items, but they have key differences in terms of mutability, syntax, performance, and use cases.

# 1. Mutability

# List: Mutable (can be modified after creation).
# You can add, remove, or change elements.
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying is allowed
my_list.append(4)  # Adding is allowed

# Tuple: Immutable (cannot be modified after creation).
# Once created, you cannot add, remove, or change elements.
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ Error: 'tuple' object does not support item assignment

# 2. Syntax

# List: Uses square brackets [].
my_list = [1, 2, 3]

# Tuple: Uses parentheses () (but parentheses are optional in some cases).
my_tuple = (1, 2, 3)
# Or even without parentheses (comma makes it a tuple)
my_tuple = 1, 2, 3


# 3. Performance
# Tuples are generally faster than lists because they are immutable and stored more efficiently in memory.

# Lists are slower for iteration and consume more memory due to their dynamic nature.

""""
4. Use Cases
Use Case	List	Tuple
Modifiable collection	✅ Yes	❌ No
Fixed collection (e.g., days of the week)	❌ No	✅ Yes
Hashable (can be a dictionary key)	❌ No (lists are unhashable)	✅ Yes
Function arguments & return values (fixed size)	❌ No	✅ Yes
Storing heterogeneous data (different types)	✅ Yes	✅ Yes
"""

# 5. Example Comparisons
# List (Mutable)
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Allowed
fruits.append("orange")  # Allowed

# Tuple (Immutable)
colors = ("red", "green", "blue")
colors[1] = "yellow"  # ❌ Error


# When to Use Which?
# Use a List when you need a dynamic collection that changes over time (e.g., appending, removing elements).

# Use a Tuple when you need a fixed collection (e.g., coordinates, database records) or hashable keys in dictionaries.

