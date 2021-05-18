# Snak, gun or water game

import random

def gamewin(comp, you):
    # if to value are eqal, declare a tie!
    if comp == you:
        return None
    # Check for all posiblities when computer chouse s    
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # Check for all posiblities when computer chouse w           
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # Check for all posiblities when computer chouse g           
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

a = input("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randno = random.randint(1, 3)               # every time display rendom value
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("Your's Turn: Snake(s) Water(w) or Gun(g)?")
a = gamewin(comp, you)

print(f"Computer chose {comp}")
print(f"Your chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!") 
else:
    print("You Lose!") 

