import random
n = random.randint(1,100) 

a = -1
guesses = 0

while(a != n):
  
  a = int(input("Guess The Number: "))
  if(a>n):
    print("Lower Number Please")
    
  elif(a<n):
    print("Higher Number Please")
    guesses +=1    

print(f"You Have Guessed The Number {n} Correctly In {guesses} Attempts")