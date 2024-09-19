

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    valid = ['A', 'B', 'C', 'D']
    
    # check for no items added
    if skus == "":
        return 0
    
    # loop through SKUS, return -1 if any characters not valid
    for char in skus:
        # check char is valid
        if char not in valid:
            return -1 
    
    return -1

