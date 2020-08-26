import time
import math
import keyboard

# Betting Breakdown
initFee = 1500000
prefCard = 500000
infamous = 3000000
safe1 = 1000000
safe2 = 3300000
safe3 = 6500000

target = 1000000000
ct = 1

print(f'\nWelcome to your grind-less \'Golden Grin Anonymous\' Achievement!\n')

currentSpend = int(input('What is your current spend amount?  $').replace(',',''))
leftToSpend = '{:,}'.format(target - int(currentSpend))
print(f'OK, You have ${leftToSpend} left to spend.')

safedCards = int(input('\nHow many cards do you have safed? '))
isitInfamous = input('Is It Infamous? (y/n) ').upper()

if safedCards == 0:
    spin = initFee
elif safedCards == 1:
    spin = initFee + prefCard + safe1
elif safedCards == 2:
    spin = initFee + prefCard + safe1 + safe2
else:
    spin = initFee + prefCard + safe1 + safe2 + safe3

if isitInfamous == 'Y':
    spin += infamous

numSpins = math.ceil(currentSpend / spin)

def spinThatWheel():
    global ct
    while keyboard.is_pressed('q') == False:
        while ct <= numSpins:
            print(f'Spin {ct}/{numSpins}.')
            keyboard.press('space')
            time.sleep(0.5)
            keyboard.release('space')
            time.sleep(7)
            keyboard.press('enter')
            time.sleep(0.5)
            keyboard.release('enter')
            time.sleep(2)
            ct += 1

print(f'\nAt your current settings you would need {numSpins} card turns to reach the target.')
start = input('Are you ready to start? (y/n) ').upper()

if start != 'Y':
    print('\nThanks for playing.')
else:
    print('\nLoad the game, enter your settings into Offshore Payday')
    print('Press any key to start...')
    keyboard.read_key()
    print('HOLD \'Q\' to quit.')
    spinThatWheel()
    

