import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([0,-1,1])
you = input("Enter your choice: ")
youDict= {"s":1,"w":-1,"g":0}
revDict= {1:"Snake",-1:"Water",0:"Gun"}
youNum= youDict[you]

print("You chose",revDict[youNum])
print("\nComputer chose",revDict[computer])

if(computer==youNum):
    print("It's a draw")
else:
    if (computer == -1 and youNum == 1):
        print("You Win!")
    elif (computer == -1 and youNum == 0):
        print("You Lose!")
    elif (computer == 1 and youNum == -1):
        print("You Lose!")
    elif (computer == 1 and youNum == 0):
        print("You Win!")
    elif (computer == 0 and youNum == -1):
        print("You Win!")
    elif (computer == 0 and youNum == 1):
        print("You Lose!")
    else:
        print("Something went wrong")

