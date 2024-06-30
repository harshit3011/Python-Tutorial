from PyDictionary import PyDictionary
import pyttsx3
import os

# 1. Write a program to print Twinkle twinkle little star poem in python.
# 2. Use REPL and print the table of 5 using it.
# 3. Install an external module and use it to perform an operation of your interest.
# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

# 1
# print('''Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.
#
# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.''')

# 3.
# dictionary = PyDictionary()
# print(dictionary.meaning("improvisation"))



# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

#4 
directory_path = '/'
contents = os.listdir(directory_path)

for item in contents:
    print(item)