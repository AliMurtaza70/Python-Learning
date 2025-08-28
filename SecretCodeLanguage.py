import random

def encode(name):
    first_letter = name[0]
    random_chars = ''.join(random.sample(name, 3))
    newWord = name[1:]
    name = random_chars + newWord + random_chars + first_letter

    return name

def decode(name):
    last_letter = name[-1]
    newWord = name[3:-4]
    name = last_letter + newWord

    return name

word = input("Enter a word: ")
method = input("In which method you want to convert the word Encoding or Decoding: ")

if(method == "Encoding"):
    if(word.__len__() < 3):
        reverseWord = word[::-1]
        print(reverseWord)
    else:
        print(encode(word))
elif(method == "Decoding"):
    if(word.__len__() < 3):
        reverseWord = word[::-1]
        print(reverseWord)
    else:
        print(decode(word))



# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Enoding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to encode or decode
