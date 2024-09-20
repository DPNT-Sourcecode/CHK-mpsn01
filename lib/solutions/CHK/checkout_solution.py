

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    # check for no items added
    if skus == "":
        return 0
    
    # initialise a class to represent the checkout
    checkout = Checkout()
    
    # loop through SKUS, return -1 if any characters not valid
    #
    # note: there are a bunch of places we could put the validation. 
    # I'm just going to have it at top level to save time, but
    # it could also be in either the Checkout class or the Item 
    # class.
    valid = ['A', 'B', 'C', 'D', 'E']
    for char in skus:
        # check char is valid
        if char not in valid:
            return -1
        
        # Call checkout.add_item() for each char
        checkout.add_item(char)
        
    return checkout.total()

# Class is used to represent the checkout
class Checkout:
    def __init__(self):
        self.items = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
        self.receipt = {}
        
    def add_item(self, name: str):
        if name not in self.receipt:
            # Intialise a new item in the receipt
            self.receipt[name] = Item(name, self.items[name])
        
        self.receipt[name].add_one()
        
    def remove_item(self, name: str):
        if name not in self.receipt:
            return # nothing to be done here
        
        self.receipt[name].remove_one()
        if self.receipt[name].count == 0:
            del self.receipt[name] # Remove if count reaches
            
    def get_multi_item_discount(self) -> int:
        if len(self.receipt) == 0:
            return 0
        
        if 'E' not in self.receipt or 'B' not in self.receipt:
            return 0 
        
        num_e_items = self.receipt['E'].count
        num_b_items = self.receipt['B'].count
        
        # Apply 2E free B discount first    
        num_discounts_available = num_e_items // 2
        free_b_items = min(num_discounts_available, num_b_items)
        discount = free_b_items *self.items['B']
        
        # Calculate discount on remaining B items
        remaining_b_items = num_b_items - free_b_items
        num_b_discount_pairs =  remaining_b_items // 2
        discount += num_b_discount_pairs * 15
                         
        return discount
            
    def total(self) -> int:
        sum = 0
        for item in self.receipt.values():
            sum = sum + item.total()
            
        return sum - self.get_multi_item_discount()

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
            total = 0
            num_items = self.count
            
            # see how many sets of five there are
            num_quintuplets = num_items // 5
            num_items_remainder = num_items % 5
            total += num_quintuplets * 200 
            
            # now see how many sets of three
            num_triplets = num_items_remainder // 3
            remainder = num_items_remainder % 3
            total += num_triplets * 130
            
            # and the remainder
            total += remainder * self.price
            
            return total
        
        return self.count*self.price
