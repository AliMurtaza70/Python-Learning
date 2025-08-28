# Opening a File
# Before performing any operations on a file, it must be opened using the open() function.
# Syntax: open(filename, mode)

f = open('myfile.txt', 'r')  # Open a file for reading

# By default, open() returns a file object used to read from or write to the file, depending on the mode.


# Modes in File

# 'r'   - Read mode: Opens file for reading (default). Raises error if file doesn't exist.
# 'w'   - Write mode: Opens file for writing. Creates file if it doesn't exist, overwrites if it does.
# 'a'   - Append mode: Opens file for appending. Creates file if it doesn't exist.
# 'x'   - Create mode: Creates file, raises error if file already exists.
# 't'   - Text mode: Default mode, used for text files. No difference between 'r' and 'rt', or 'w' and 'wt'.
# 'b'   - Binary mode: Used for binary files like images, PDFs, etc.


# Reading from a File
# Use the read() method to read the entire content of the file as a string.

f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
f.close()  # Always close the file after use


# Writing to a File
# Open the file in write mode to overwrite its contents or create a new file.

f = open('myfile.txt', 'w')
f.write('Hello, world!')
f.close()

# Appending to a File
# Open the file in append mode to add content without overwriting existing data.

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()


# Closing a File
# Use the close() method to release the file resources.

f = open('myfile.txt', 'r')
# ... do something with the file
f.close()


# Using the 'with' Statement
# Automatically handles closing the file after the block is executed.

with open('myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)  # No need to call f.close()
