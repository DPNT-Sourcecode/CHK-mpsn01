

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
        self.items = {'A':50, 'B':30, 'C':20, 'D':15}
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
    def __init__(self, name: str, price: int):
        self.name = name
        self.count = 0
        self.price = price
        
    def add_one(self):
        self.count += 1

    def remove_one(self):
        if self.count > 0: 
            self.count -= 1
        
    def total(self) -> int:
        # Check for discount needed to item A
        if self.name == 'A':
            return -1
        
        # Check for discount needed to item B
        if self.name == 'B':
            return -1
        
        return self.count*self.price
