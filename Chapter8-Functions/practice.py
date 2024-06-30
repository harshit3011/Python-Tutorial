# 1. Write a program using functions to find greatest of three numbers.
# 2. Write a python program using function to convert Celsius to Fahrenheit.
# 3. How do you prevent a python print() function to print a new line at the end.
# 4. Write a recursive function to calculate the sum of first n natural numbers.
# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
# 6. Write a python function which converts inches to cms.
# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
# 8. Write a python function to print multiplication table of a given number.


# 1.
# def greatest(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         return num1
#     elif(num2>num1 and num2>num3):
#         return num2
#     elif(num3>num1 and num3>num1):
#         return num3
#
# n1=int(input("Enter number 1"))
# n2=int(input("Enter number 2"))
# n3=int(input("Enter number 3"))
#
# print("Greatest number is:",greatest(n1,n2,n3))


# 2.
# def convert(temp):
#     return (temp*9/5) + 32
#
# temp=float(input("Enter the temerature in celsius: "))
# print("Temp in farhenheit is: ",convert(temp))


# 4.
# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
#
# num=int(input("Enter the number: "))
# print("Sum on n natural numbers:",sum(num))


7.

def strip(list,word):
    return [w.strip() for w in list if w.strip()!=word]

list=["  hello  ", "world", "  example  ", "test", "  hello", "example "]
target = "example"

print(strip(list,target))