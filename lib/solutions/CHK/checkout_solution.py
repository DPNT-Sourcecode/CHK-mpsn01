

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    # check for no items added
    if skus == "":
        return 0
    
    # loop through SKUS, return -1 if any characters not valid
    valid = ['A', 'B', 'C', 'D']
    for char in skus:
        # check char is valid
        if char not in valid:
            return -1
        
    # Initialise a class to represent the checkout
    checkout = Checkout(skus) 
    
    return checkout.total()

# Class is used to represent the checkout
class Checkout:
    def __init__(self, skus: str):
        # receipt stores a dict of item objects
        self.receipt = {}
    def add_item(self):
        pass
    def remove_item(self):
        pass
    def total(self) -> int:
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


