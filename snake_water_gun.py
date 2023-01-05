import random

def check(mine,c):
    if(c==mine):
        print("DRAW")
    elif(  mine=='s'and c=='w'):
        print("WIN")
    elif(mine=='w'and c=='g'):
        print("WIN")
    elif(mine=='g' and c=='s'):
        print("WIN")
    else:
        print("LOOSE")

print("snake-s\nwater=w\ngun=g")
choice=('s','w','g')
c=random.randint(0,2)
c=choice[c]
mine=input("choose ur choice:")
print("computer choice:",c)
check(mine,c)
