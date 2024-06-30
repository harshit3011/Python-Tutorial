# 1. Write a program to find the greatest of four numbers entered by the user.
# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
# 4. Write a program to find whether a given username contains less than 10
# characters or not.
# 5. Write a program which finds out whether a given name is present in a list or not.
# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
# 7. Write a program to find out whether a given post is talking about “Harry” or not.



# 1.
# num1=int(input("Enter number: "))
# num2=int(input("Enter number: "))
# num3=int(input("Enter number: "))
# num4=int(input("Enter number: "))
#
# if(num1>num2 and num1>num3 and num1>num4):
#     print("Greatest number is: ",num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("Greatest number is: ",num2)
# elif(num3>num2 and num3>num1 and num3>num4):
#     print("Greatest number is: ",num3)
# elif(num4>num2 and num4>num3 and num4>num1):
#     print("Greatest number is: ",num4)

# 2.
# sub1=int(input("Enter marks: "))
# sub2=int(input("Enter marks: "))
# sub3=int(input("Enter marks: "))
#
# avg=(sub1+sub2+sub3)/3
#
# if(sub1>=33 and sub2>=33 and sub3>=33 and avg>=40):
#     print("Passed the test")
# else:
#     print("Failed")


# 3.
# spam=input("Enter the message: ")
# if(spam.__contains__("make a lot of money") or spam.__contains__("buy now") or spam.__contains__("subscribe this") or spam.__contains__("click this")):
#     print("It is a spam message")
# else:
#     print("Message is ok")


# 4.
# username='Harry3011'
# if(len(username)<10):
#     print("Valid")
# else:
#     print("Invalid")


# 5.
# names=["Harry","Sheldon","Leonard","Barney","Jim"]
# name= input("Enter the name: ")
# if(names.__contains__(name)):
#     print("List contains",name)
# else:
#     print(name+" is not present")

7.

post=input("Enter the post: ")
if("Harry" in post):
    print("Post is about Harry")
else:
    print("Post is not about Harry")