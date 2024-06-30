# def greet(name):
#     message= "Greetings"+" "+name
#     print(message)
#
# greet("Harry")


# def avg(a,b,c):
#     return (a+b+c)/3
#
# print(avg(1,4,7))

def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)

print(factorial(5))