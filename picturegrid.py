from time import sleep

grid = [['M', 'M', '.', '.', '.', '.', '.', 'M', 'M', '.', 'A', 'A', 'A','A', 'A', 'A', 'A', '.', '.'],
        ['M', '.', 'M', '.', '.', '.', 'M', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', 'M', '.', 'M', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', '.', 'M', '.', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', '.', '.', '.', '.', '.', 'M', '.', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '.','.'],
        ['M', '.', '.', '.', '.', '.', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', '.', '.', '.', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', '.', '.', '.', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.'],
        ['M', '.', '.', '.', '.', '.', '.', '.', 'M', '.', 'A', '.', '.', '.', '.', '.', 'A', '.','.']]
        
#todo tentar usar o enumerate:

for i in range(len(grid)):
    for j in range(len(grid[0])): 
        print(grid[i][j].replace('.',' '), end='', flush=True)
        sleep(0.05)
    print()
#