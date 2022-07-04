from random import choice
from time import sleep


def typingEffect(sentence):
    """
    Aquele efeito de letra por letra
    """
    sentence = str(sentence)
    for i in sentence:
        print(i, end= '', flush= True)
        sleep(0.05)
        

def continuar(variável, condição_pro_loop, pergunta):
    variável = ' '
    while True: 
        if variável not in f'{condição_pro_loop}':
            variável = str(input(pergunta)).upper()[0] 
        elif variável in 'Y':
            player = str(input('What you choose? Rock, Paper or Scissor? ')).upper()[0]
        else: 
            break


computer = choice(['ROCK', 'PAPER', 'SCISSOR'])
print(computer)

typingEffect('Everyone knows this game, I hope you enjoy it!\n')
typingEffect('What you choose? Rock, Paper or Scissor? ')
player = str(input()).upper()
while True: 
    #como foi colocado um 'in' ao invés de '==' se o usuário escrever de maneira aleatória pode dar uns erros 
    if player in 'ROCK' and computer in 'SCISSOR' or player in 'PAPER' and computer in 'ROCK' or player in 'SCISSOR' and computer in 'PAPER':
        typingEffect('You won!\n')
    elif player == computer: 
        typingEffect('We have a tie!\n')
    else:
        typingEffect('you lose\n') 
    continuar('restart', 'YN', 'One more? (Y/N) ')
    
    
#todo a segunda partida entra em loop infinito