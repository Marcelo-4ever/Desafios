
def comma(my_list):
    """
    return all elements from a list separated by a comma
    if there is not any elements it will just print out the list itself
    if there is only one element the function will print the element
    if there are more than one elements we will have a for loop to print all elements formatted like: 1,2,3,4,5 and 6
    """
    if len(my_list) == 0:
        print(my_list)
    elif len(my_list) == 1:
        print(my_list[0])
    else:
        for i in my_list:
            if i in my_list[:-2]:
                print(f"{i}, ", end="")
            elif i in my_list[-2]:
                print(f"{i} and ", end="")
            elif i in my_list[-1]:
                print(i)


animals = ['fdsf','sfsdfsd','fsdfsd'] #-> esse exemplo ficou como: fsdf, fdsfds and sdfdsfds and -> tem que tirar esse último 'and'
comma(animals)
