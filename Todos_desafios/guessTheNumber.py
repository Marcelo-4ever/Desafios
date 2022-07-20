"""
Create a function where your program will 'think' 10 different numbers and the user will try to get the answer right as many times as he needs. 
"""
from random import randint
from time import sleep

from termcolor import colored


def typingEffect(string):
    string = str(string)
    for i in string:
        print(i, end="", flush=True)
        sleep(0.05)


def typingEffectColors(string):
    string = str(string)
    string = colored(string, "cyan") #change the color of the entire sentence
    for i in string:
        print(i, end="", flush=True)
        sleep(0.05)


def acertarNúmero(num):
    """
    Function that happen until the number of games is done.
    """
    attempts = 0  # variable that will works to count how many attempts the user tried before he got the answer right
    for j in range(matches): #how many games the user chose
        if j < matches: #if J is smaller than we have all this code. Example: matches = 2 -> 0 < 2 -> 1 < 2 -> 2 < 2? -> it's over
            computer = randint(0, 10)
            while True:
                
                attempts += 1
                if num == computer:
                    finished = f"You are lucky! You got me this time!\nTotal attempts {attempts} "
                    typingEffectColors(finished)
                    attempts = 0
                    break
                
                if num < computer:
                    low = "You should try higher sometimes, don't be afraid!"
                    typingEffectColors(low)
                    num = int(input("\nChoose a number: "))
                
                elif num > computer:
                    high = ("Hey hey! Try to low your numbers, this one was way too high!")
                    typingEffectColors(high)
                    num = int(input("\nChoose a number: "))
        
        if (j < matches - 1):  # tive que fazer dessa forma pois já existe uma pergunta fora do loop, logo ficaria uma pergunta sobrando
            num = int(input("\n\nChoose a number: "))


n = "This is the Guess The Number game. Are you ready? I hope so! \n"
typingEffect(n)
games = "How many games you want to play? "
typingEffect(games)
matches = int(input())
user = int(input("\nChoose a number between 0 and 10: "))
acertarNúmero(user)
