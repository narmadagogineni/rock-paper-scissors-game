# Rock, Paper and Sissors

import random

def gameWin(computer, you):
    if computer == you:
        return None

    elif computer =='r':
        if you =='p':
            return False
        elif you=='s':
            return True

    elif computer =='p':
        if you =='s':
            return False
        elif you=='r':
            return True

    elif computer =='s':
        if you =='r':
            return False
        elif you =='p':
            return True                        

print("Computer's turn: Rock(r) Paper(p) or Sissors(s)?")
randNum = random.randint(1, 3)
if randNum == 1:
    computer = 'r'
if randNum == 2:
    computer = 'p'    
if randNum == 3:
    computer = 's'    

you = input("Your turn: Rock(r) Paper(p) or Sissors(s)?")
a = gameWin(computer, you)

print(f'Computer chose {computer}')
print(f'You chose {you}')

if a == None:
    print('The game is a tie')
elif a:
    print('Hurray, You won!')
else:
    print('Aigoo, You lost!')