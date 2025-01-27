import random

computer = random.choice([-1, 0, 1])

youStr = input("Enter Your Choice : ")
youDict = {"s": 1, "w": -1, "g":0}
reverseDict = {1: "Snake", -1:"Water", 0: "Gun"}

you = youDict[youStr]

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if(computer == you):
    print("Game Draw")

else:
    if(computer ==-1 and you ==1):
        print("You Win")
    
    elif(computer ==-1 and you ==0):
        print("You Lose")
    
    elif(computer ==1 and you ==-1):
        print("You Lose")
    
    elif(computer ==1 and you ==0):
        print("You Win")
    
    elif(computer ==-1 and you ==-1):
        print("You Win")
    
    elif(computer ==0 and you ==1):
        print("You Lose")
    
    else:
        print("Something Went Wrong")    

