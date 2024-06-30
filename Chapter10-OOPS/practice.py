# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
# 4. Add a static method in problem 2, to greet the user with hello.
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


2.

class Calculator:
    def square(self,num):
        self.num=num
        print(pow(self.num,2))

    def cube(self,num):
        self.num=num
        print(pow(self.num,3))

    def root(self,num):
        self.num=num
        print(pow(self.num,1/2))

num=Calculator()
num.square(4)
num.cube(4)
num.root(4)
