# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"


# 1.
#
# name=input("Enter your name:")
# print(f"Good Afternoon {name}")

# 2.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
#  '''
#
# print(letter.replace("<|Name|>","Harry").replace("<|Date|>","29th June"))

# 3
# str="Hello  world"
# print(str.__contains__("  "))
# print(str.find("  "))

# 4.
# str="Hello  world"
# print(str.replace("  "," "))

5.
letter = "Dear \'Harry\', this python course is nice.\nThanks!"
print(letter)