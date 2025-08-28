# 🔄 What is an Alternative Constructor?
# Normally, we create an object using the __init__ method.

# But sometimes, the data we get isn't ready to pass directly to __init__.

# For example, we might get a string like "John-24", and we need to convert/split it before creating the object.

# Instead of repeating .split() every time, we can create a special method to handle this — that’s an alternative constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 👇 This is an alternative constructor
    @classmethod
    def from_string(cls, string):
        name, age = string.split("-")
        return cls(name, int(age))  # 👈 creates a new Person object

# Regular way of creating object
a1 = Person("Harry", 22)
print(a1.name)  
print(a1.age)

# Creating object from a string using the alternative constructor
person_data = "John-24"
a2 = Person.from_string(person_data)
print(a2.name)  
print(a2.age)
