# readlines() method
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f = open('myfile2.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
# The readlines() method reads all the lines of the file and returns them as a list of strings.

# writelines() method
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# Here's an example of how to use the writelines() method:

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
# This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()
# It is also a good practice to close the file after you are done with it.

f = open('myfile2.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)


# seek() function
# The seek() function allows you to move the current position within a file to a specific byte.
# You can move forward or backward based on the byte offset provided.

with open('file.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes from that position
    data = f.read(5)


# tell() function
# The tell() function returns the current byte position within the file.
# It's useful for tracking or bookmarking the current location in the file.

with open('file.txt', 'r') as f:
    # Read the first 10 bytes
    data = f.read(10)

    # Save the current position in the file
    current_position = f.tell()

    # Seek to the saved position (redundant here but useful in workflows)
    f.seek(current_position)


# truncate() function
# The truncate() function is used to resize a file to a specific number of bytes.
# If the specified size is smaller than the current file size, the extra data is lost.

with open('sample.txt', 'w') as f:
    f.write('Hello World!')   # Write 12 bytes to the file
    f.truncate(5)             # Truncate file to first 5 bytes ('Hello')

# Reading the truncated content
with open('sample.txt', 'r') as f:
    print(f.read())           # Output: Hello
