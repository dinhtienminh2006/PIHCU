import random
import time
import os 
money = int(input('your money want to charge:'))
while True:
    player = input('tai or xiu')
    player = player.lower()
    bets = int(input('your bets you want to play[ the bets not be large than the money charge!]'))
    money = money - bets
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    total = dice1 + dice2 + dice3
    print('result:')
    print('dice1 is:',time.sleep(2),dice1)
    print('dice2 is:',time.sleep(2),dice2)
    print('dice3 is:',time.sleep(2),dice3)
    print('The total of three dice is:', time.sleep(2),total)
    if (player == 'tai' or player == 'Tai') and total > 10:
        print('You win by your choice',player)
        print('You will be receive %4.0f' %(money + bets*198/100))
    else:
        print('You lose by your choice',player)
        print('Your money remaining %4.0f' %(money))

    choose = input('You want to [play] or [stop]')
    if choose == 'stop':
        os.system('cls')
        break
