import random
# # 🧠 Exercise: Odd or Even Number Checker
# # Task:
# # Write a Python program that does the following:

# # Asks the user to enter a number.

# # Checks if the number is odd or even.

# # Prints whether the number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is a Even number")
else:
    print(f"{number} is a Odd number")

# # 🧠 Exercise: Simple Calculator
# # Task:
# # Write a Python program that:

# # Asks the user to enter two numbers.

# # Asks the user to choose an operation: +, -, *, or /.

# # Performs the chosen operation on the two numbers.

# # Prints the result.

valueToMultiply = int(input("Enter a value to multiply: "))
valueToMultiplyBy = int(input("Enter a value to multiply by: "))
operationSign = input("Enter the operation sign: ")

if operationSign == "+":
    print(f"{valueToMultiply} + {valueToMultiplyBy} = {valueToMultiply + valueToMultiplyBy}")
elif operationSign == "-":
    print(f"{valueToMultiply} - {valueToMultiplyBy} = {valueToMultiply - valueToMultiplyBy}")
elif operationSign == "*":
    print(f"{valueToMultiply} * {valueToMultiplyBy} = {valueToMultiply * valueToMultiplyBy}")
elif operationSign == "/":
    print(f"{valueToMultiply} / {valueToMultiplyBy} = {valueToMultiply / valueToMultiplyBy}")
else:
    print("Invalid operation sign")


# # 🧠 Exercise: FizzBuzz
# # Task:
# # Write a Python program that:

# # Asks the user to enter a number n.

# # Prints numbers from 1 to n, but:

# # For multiples of 3, print "Fizz" instead of the number.

# # For multiples of 5, print "Buzz" instead of the number.

# # For multiples of both 3 and 5, print "FizzBuzz".



n = int(input("Enter a number: "))

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 🎯 New Challenge: Number Guessing Game
# Task:
# Write a program that:

# Randomly picks a number between 1 and 100.

# Asks the user to guess the number.

# Tells the user if their guess is too low, too high, or correct.

# Repeats until the user guesses correctly.

# At the end, print how many attempts it took.

randomNumber = random.randint(1,100)
userGuess = int(input("Enter a guess: "))
attempts = 1

while userGuess != randomNumber:
    if userGuess < randomNumber:
        print("Too low")
    else:
        print("Too high")
    userGuess= int(input("Guess the number again: "))
    attempts += 1

print(f"You guessed the number in {attempts} attempts \n The number was {randomNumber}")


# 🧠 Exercise: Student Grade Tracker
# Task:
# Create a Python program that:

# Lets the user enter the names and scores of 5 students.

# Stores the data in a list of dictionaries like:

# [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}, ...]

# Has a function that:
# Takes the list of students.
# Calculates and returns the average score.
# After input, print:

# Each student’s name and score.
# The average score.
# The name(s) of the top-scoring student(s).

students = []

for i in range(2):
    name = input("Enter the name of the student: ")
    score = int(input("Enter the score of the student: "))
    students.append({"name": name, "score": score})

def calculateAverage(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)

average = (calculateAverage(students))
print(f"The average score is {average:.2f}")

print("\nStudent Scores:")
for student in students:
    print(f"{student['name']}: {student['score']}")


# Find the top score
top_score = max(student["score"] for student in students)

# Find all students with the top score (to handle ties)
top_scorers = [student["name"] for student in students if student["score"] == top_score]

# Print top scorer(s)
print(f"Top scorer(s): {', '.join(top_scorers)} with a score of {top_score}")