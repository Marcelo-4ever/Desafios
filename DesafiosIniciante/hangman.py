"""Objetivo: c _ _ _ _, ca_ _ _, carr _, carro"""
from random import choice
import sys
#from time import sleep
palavra_secreta = ('carro', 'barco')
acertou = 0
letras_certas = ''
for palavra in palavra_secreta:
    print()
escolha = choice(palavra_secreta)
print(f'O computador escolheu {escolha}') #escolha do computador
while True:
    usuário = str(input('\nLetra: '))
    for pos, l in enumerate(escolha): #pegar letra por letra, e enumerar cada uma
        if usuário in l: 
            acertou += 1
            letras_certas += usuário
            print(f'{letras_certas}', end= ' ')
            if acertou == len(escolha): 
                sys.exit()
        else:
            print('_', end= ' ')
    
