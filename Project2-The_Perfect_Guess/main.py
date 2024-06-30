import random

'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
'''

def rand():
    num=random.randint(1,100)
    return num

guesses=0
flag=True
number=rand()
for i in range(10):
    user=int(input("Enter your guess: "))
    guesses+=1
    if(user==number):
        flag=False
        print("Correctly guessed! Number of guesses it took:",guesses)
        break
    elif(user>number):
        print("Enter a lower number")
    else:
        print("Enter a higher number")


if(flag==True):
    print("You couldn't guess the number!")