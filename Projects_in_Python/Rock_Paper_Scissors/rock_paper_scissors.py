import random

def gameWin(comp,you):
    if(comp==you):
        return None
    if(comp=='r'):
        if(you=='p'):
            return False
        if(you=='s'):
            return True

    if(comp=='p'):
        if(you=='s'):
            return False
        if(you=='r'):
            return True

    if(comp=='s'):
        if(you=='p'):
          return False
        if(you=='r'):
         return True


print(" Welcome to Rock,Paper and scissor Game! ")
comp=print("Computer's Turn:Rock(r) Paper(p)  Scissor(s)?")
randoNo=random.randint(1,3)
if(randoNo==1):
    comp='r'
elif(randoNo==2):
    comp='p'
elif(randoNo==3):
    comp='s'

you=input("Player's 2 Turn:Rock(r) Paper(p)  Scissor(s)?")

a=gameWin(comp,you)
print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if(a==None):
    print("The gane is a Tie")
elif(a==True):
    print("You win")
else:
    print("You Loose")