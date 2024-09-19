

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    result = 0
    valid = ['A', 'B', 'C', 'D']
    
    # check for no items added
    if skus == "":
        return 0
    
    # TODO: Initialise a class to represent the checkout
    checkout = Checkout()
    
    # loop through SKUS, return -1 if any characters not valid
    for char in skus:
        # check char is valid
        if char not in valid:
            return -1 
    
    return result

# Class is used to represent the checkout
class Checkout:
    def __init__(self):
        pass
    def add_item(self):
        pass
    def remove_item(self):
        pass
    def total(self):
        pass

# Class is used to represent an item, how much it costs
# and how many have been selected
class Item:
    def __init__(self):
        pass
    def add_one(self):
        pass
    def remove_one(self):
        pass
    def total(self):
        pass
