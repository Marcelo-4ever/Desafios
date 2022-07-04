def addToInventory(inventory, addtoinventory):
    """
    We have the inventory itself and the items to add to this inventory(addtoinventory)
    The loop for goes through all items that will be added -> if the item is in the inventory already, since we have a dictionary, we do this: inventory[item] += 1, so it's value will increase in 1. 
    If the item is not find in the inventory we add it like this: inventory[item] = 1, since it's the first time, after this it will be in the dictionary and the condition change in case it appears again
    """
    for i in addtoinventory:
        if i not in inventory:
            inventory[i] = 1
        elif i in inventory:
            inventory[i] += 1
        

def displayInventory(inv):
    print('Inventory: ')
    total = 0
    for k, v in inv.items(): 
        print(f'{v} {k}')
        total += v
    print(f'Total number of items: {total}')
    
    
inv = {'gold coin': 20, 'dagger': 1} #inventory 
new_inv = ['gold coin', 'dagger', 'knife', 'wood', 'wood', 'wood', 'wood', 'wood', 'Big Sword', 'Small dagger'] #items to add in the inventory

addToInventory(inv, new_inv)
displayInventory(inv)