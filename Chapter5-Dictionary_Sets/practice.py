# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# 5. s = {}
# What is the type of 's'?
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}





# 1.
# dic={
#     "chalna":"walk",
#     "dekhna":"see",
#     "chadna":"climb",
#     "udna":"fly"
# }
#
# word=input("Enter the word you want: ")
# print(dic[word])

# 2.
# s=set()
# num1=int(input("Enter the number: "))
# s.add(num1)
# num2=int(input("Enter the number: "))
# s.add(num2)
# num3=int(input("Enter the number: "))
# s.add(num3)
# num4=int(input("Enter the number: "))
# s.add(num4)
# num5=int(input("Enter the number: "))
# s.add(num5)
# num6=int(input("Enter the number: "))
# s.add(num6)
# num7=int(input("Enter the number: "))
# s.add(num7)
# num8=int(input("Enter the number: "))
# s.add(num8)
# print("Unique numbers are:\n")
# print(s)

# 3.
# s=set()
# s.add(20)
# s.add('20')
# print(s)

# 4.
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))
# print(s)

# 5.
# s={}
# print(type(s))

# 6.
# dict={}
# name1= input("Enter Friend's name: ")
# lang1= input("Enter language: ")
# dict.update({name1:lang1})
#
# name2= input("Enter Friend's name: ")
# lang2= input("Enter language: ")
# dict.update({name2:lang2})
#
# name3= input("Enter Friend's name: ")
# lang3= input("Enter language: ")
# dict.update({name3:lang3})
#
# name4= input("Enter Friend's name: ")
# lang4= input("Enter language: ")
# dict.update({name4:lang4})

# print(dict)


