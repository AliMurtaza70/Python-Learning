# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3

# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.

# Class Method
# Class methods are methods that are bound to the class and not the instance of the class. They have access to the class variables and can modify them. They are defined using the @classmethod decorator.




class Employee:
    company = "Google"
    def show(self):
        print(f"The {self.name} Employee belongs from this {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Raj"
e1.show()
e1.changeCompany("Microsoft")
e1.show()
print(Employee.company)