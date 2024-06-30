import random


# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.
# 5. Repeat program 4 for a list of such words to be censored.
# 6. Write a program to mine a log file and find out whether it contains ‘python’.
# 7. Write a program to find out the line number where python is present from ques 6.
# 8. Write a program to make a copy of a text file “this. txt”
# 9. Write a program to find out whether a file is identical & matches the content of
# another file.
# 10. Write a program to wipe out the content of a file using python.
# 11. Write a python program to rename a file to “renamed_by_ python.txt.



# 1.
#
# f=open("poems.txt","r")
# data = f.read()
# print(data.__contains__("twinkle"))


# 2.
#
# def game():
#     start=1
#     end=100
#     return random.randint(1,100)
#
# score=game()
# with open("Hiscore.txt", "r") as f:
#     hi_score = f.read()
#
# if hi_score:
#     hi_score = int(hi_score)
# else:
#     hi_score = 0
#
# if score > hi_score:
#     with open("Hiscore.txt", "w") as f:
#         f.write(str(score))
#     print(f"New hi-score: {score}")
# else:
#     print(f"Current hi-score remains: {hi_score}")



# 4.
# file=open("donkey.txt","r")
# content = file.read()
# with open("donkey.txt", 'w') as file:
#     pass
# content=content.lower().replace("donkey","#####")
# with open("donkey.txt","a") as file:
#     file.write(content)
#

