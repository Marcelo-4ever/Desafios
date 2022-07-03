from time import sleep
def zizZag(): 
    while True:
        x = 15
        try: 
            dots = '...........'
            for i in range(x+1):
                print(f"{' ' * i}{dots}")
                sleep(0.2)
                if i == x: 
                    for j in range(x+1):
                        j = x - j 
                        print(f"{' ' * j }{dots}")
                        sleep(0.2)
        except KeyboardInterrupt: 
            print('Valeu por jogar irmão!')
            break
zizZag()