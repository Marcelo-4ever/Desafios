
def displayGame(x):
    """
    We use 'for' loop and this in all items(key-pair values). We just need to format to display in the screen as we want """
    print('Inventory:')
    total = 0 
    for k, v in x.items():
        print(f'{v} {k}')
        total += int(v)    
    print(f'Total number of items: {total}')
game = {'Bronze coins': '25', 'Silver coins': '12', 'Gold coins':'4','torch': '6', 'Rope': '1', 'Sword': '0'}
displayGame(game)