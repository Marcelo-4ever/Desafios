#Rock, paper, scissor and the player choose how many times he wants to play and is displayed on the screen the game that the player is playing "Game 1, Game 2, Game 3, etc.." 
from random import choice
from time import sleep  
games = int(input('How many games? '))
gq = 0  
while True: 
    if gq == games:
        break
    #computer choices always change
    computer = choice(['ROCK', 'PAPER', 'SCISSOR'])
    print('-'*40)
    #if the user write the names or the names wrong, the loop will repeat asking: 
    player = str(input('1 or [Rock], 2 or [Paper], 3 or [Scissor] ')).strip().upper()
    #if the user write
    if player == 'ROCK' or player == 'PAPER' or player == 'SCISSOR':
        #games quantity will be the flag 
        gq += 1 
        print('ROCK')
        sleep(0.8)
        print('PAPER')
        sleep(0.8)
        print('SCIIIISOR!')
        sleep(1.5)
        print(f'GAME {gq}: ',end=' ')
        if player == 'ROCK' and computer == 'SCISSOR' or player == 'PAPER' and computer == 'ROCK' or player == 'SCISSOR' and computer == 'PAPER':
            print('YOU WON! FANTASTIC!')
        elif player == computer: 
            print(f"IT'S A TIE, WE BOTH CHOSE {computer}" )
        else: 
            print('YOU LOSE! TRY AGAIN!')
    #if the user put numbers
    elif player in '123':
        gq += 1
        print('ROCK')
        sleep(0.8)
        print('PAPER')
        sleep(0.8)
        print('SCIIIISOR!')
        sleep(2)
        print(f'GAME {gq}:', end= ' ')
        if player == '1' and computer == 'SCISSOR' or player == '2' and computer == 'ROCK' or player == '3' and computer == 'PAPER':
            print('YOU WON. AMAZING!')
        elif player == '1' and computer == 'ROCK' or player == '2' and computer == 'PAPER' or player == '3' and computer == 'SCISSOR':
            print(f"IT'S A TIE. WE BOTH CHOSE {computer}!")
        else: 
            print('THIS TIME YOU LOSE!')    
print('-'*40)
print('GAME OVER!')        

#todo 