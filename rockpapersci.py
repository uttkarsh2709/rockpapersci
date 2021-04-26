import random
def game (comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False   
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False   
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False   


print("Computer's turn rock(r) paper(p) scissor(s)" )
randomno=random.randint(1,3)
if randomno==1:
   comp='r'
elif randomno==2:
   comp='p'
elif randomno==3:
   comp='s'
print("your turn")
you=input("Your's turn rock(r) paper(p) scissor(s)")         
a=game(comp,you)
print(f"you choose {you}")
print(f"computer choose{comp}")

if a==None:
    print("game is a tie")
elif a==True:
    print("you won")
elif a==False:
    print("you lose")    