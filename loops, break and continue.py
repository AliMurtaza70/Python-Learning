# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop


# The for Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")


# Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)


# Similarly, we can use loops for lists, sets and dictionaries.

# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

# Here, we can use the range() function.

# Example:
for k in range(5):
    print(k)

# Here, we can see that the loop starts from 0 by default and increments at each iteration.

# But we can also loop over a specific range.

# Example:
for k in range(4, 9):
    print(k)


# Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

# Example:
count = 5
while (count > 0):
    print(count)
    count = count - 1
# Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

# Example:
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

z = int(input("Enter the number: "))

while (z < 91):
    print(z)
    z = z + 9


# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

# Example
z = 0
while True:
    print(z)
    z = z + 1
    if (z % 100 == 0):
        break


# The first condition is 0 cuz 0%100 == 0 so it should break but do while execute the code ones then check the condition


# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# example
for i in range(1, 101, 1):
    print(i, end=" ")
    if (i == 50):
        break
    else:
        print("Mississippi")
print("Thank you")



# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
  



# Python - else in Loop
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too.
# The else block appears after the body of the loop.
# The statements in the else block will be executed after all iterations are completed.
# The program exits the loop only after the else block is executed.

# Syntax:
# for counter in sequence:
#     # Statements inside for loop block
# else:
#     # Statements inside else block

# Example:
for x in range(5):
    print("iteration no {} in for loop".format(x + 1))
else:
    print("else block in loop")
print("Out of loop")

# Output:
# iteration no 1 in for loop
# iteration no 2 in for loop
# iteration no 3 in for loop
# iteration no 4 in for loop
# iteration no 5 in for loop
# else block in loop
# Out of loop
