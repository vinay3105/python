import random

rand=random.randint(1,100)
guess=int(input("enter the number:"))
attempt=1
while(True):
    if(guess>rand):
        guess=int(input("try to choose lesser number:"))
        attempt+=1

    elif(guess<rand):
        
        guess=int(input("try to choose bigger number:"))
        attempt+=1

    else:
        print(f"you choose it right after {attempt} these many attempts")
        break;
