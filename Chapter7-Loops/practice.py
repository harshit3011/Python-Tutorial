# 1. Write a program to print multiplication table of a given number using for loop.
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# 3. Attempt problem 1 using while loop.
# 4. Write a program to find whether a given number is prime or not.
# 5. Write a program to find the sum of first n natural numbers using while loop.
# 6. Write a program to calculate the factorial of a given number using for loop.
# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3
# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *
# 10. Write a program to print multiplication table of n using for loops in reversed
# order.



# 1.
# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(num*i)

# 2.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print("Greetings", name)


# 4.
# num = int(input("Enter the number: "))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count+=1
#
# if not(count==2):
#     print("Number is not prime")
# else:
#     print("Number is prime")


# 5
# num = int(input("Enter the number: "))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)


# 6.
# num = int(input("Enter the number: "))
# fact=1
# for i in range(num,0,-1):
#     fact*=i
#
# print(fact)

# 7.
# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")


8.
count=1
for i in range(3):
    for j in range(count):
        print('*',end='')
    print('\n')
    count+=2