
def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1: 
        return 3 * number + 1 
        
while True: 
    try: 
        num = int(input('Write a number: '))
        print(collatz(num))
    except (ValueError): 
        print('Must be a integer type!')
    except KeyboardInterrupt:
        print('\nSee ya! ')
        break
    
#todo verificar o enunciado do desafio