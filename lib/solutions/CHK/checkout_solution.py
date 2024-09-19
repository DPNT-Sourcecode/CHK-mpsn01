

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
    checkout = Checkout() 
    
    return checkout.total()

# Class is used to represent the checkout
class Checkout:
    def __init__(self):
        self.items = {'A':50, 'B':30, 'C':20, 'D':15}
        self.receipt = {}
        
    def add_item(self, name: str):
        pass
    def remove_item(self, name: str):
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
        # Check for discount needed to item A - 3A for 130 
        if self.name == 'A':
            num_triplets = self.count // 3
            remainder = self.count % 3
            return (num_triplets * 130) + (remainder * self.price)
        
        # Check for discount needed to item B - 2B for 45
        if self.name == 'B':
            num_pairs =  self.count // 2
            remainder = self.count % 2
            return (num_pairs * 45) + (remainder * self.price)
        
        return self.count*self.price
