

# noinspection PyUnusedLocal
# skus = unicode string
import string


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
    capital_letters = (letter for letter in string.ascii_uppercase)
    valid = list(capital_letters)
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
        self.items = {
            'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20, 'H':10,
            'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 
            'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90,
            'Z': 50}
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
        discount = 0
        
        if len(self.receipt) == 0:
            return 0
        
        num_e_items = 0
        num_b_items = 0
        
        if 'E' in self.receipt:
             num_e_items = self.receipt['E'].count
        
        if 'B' in self.receipt:
            num_b_items = self.receipt['B'].count
                
        # discount values
        discount_b_pair = 15
        discount_e_pair = self.items['B']
        
        # check for free b discount
        num_e_pairs = min(num_e_items // 2, num_b_items)
        num_b_items -= num_e_pairs
        discount += num_e_pairs * discount_e_pair
        
        if num_b_items < 0:
            num_b_items = 0
            
        # apply remaining 2B for 45 discount
        num_b_pairs = num_b_items // 2
        discount += num_b_pairs * discount_b_pair
        
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
            
    # used to apply discounts in the format 2B for 45
    def apply_single_discount_offer(self):
        items = {'K':[2,150],'P': [5,200]}
        
        total = 0
        num_items = self.count
        discounts = items[self.name]
        
        # see how many of the set exists
        num_sets = num_items // discounts[0]
        remainder = num_items % discounts[0]
        total += num_sets * discounts[1]
        
        # and the remainder
        total += remainder * self.price
        return total
    
    # used to apply discounts in the format 3A for 130, 5A for 200
    def apply_double_discount_offer(self):
        # store the elible items and their discount prices and set sizes
        items = {'A':[[3,130],[5,200]],'H':[[5,45],[10,80]],'V':[[2,90],[3,130]]}
        
        total = 0
        num_items = self.count
        discounts = items[self.name]
        
        # see how many of the larger set exists
        num_larger = num_items // discounts[1][0]
        num_larger_remainder = num_items % discounts[1][0]
        total += num_larger * discounts[1][1]
        
        # now see how many of the smaller set is left 
        num_smaller = num_larger_remainder // discounts[0][0]
        remainder = num_larger_remainder % discounts[0][0]
        total += num_smaller * discounts[0][1]
       
        # and the remainder
        total += remainder * self.price
        
        return total
    
    # used to apply buy x number of items get one free discounts
    def apply_get_one_free(self):
        # store items eligible for a get one free offer and the number
        # required to get a free item.
        items = {'F': 3, 'U': 4}
    
        total = 0
        num_items = self.count 
        set_size = items[self.name]
            
        # see how many sets there are
        num_sets = num_items // set_size
        remainder = num_items % set_size
        total = (num_sets * (set_size - 1) * self.price) + (remainder * self.price)
        return total
        
    def total(self) -> int:
        total = 0
        
        # Check for discount needed to item A - 3A for 130
        if self.name == 'A' or self.name == 'H' or self.name == 'V':
            return self.apply_double_discount_offer()
        
        if self.name == 'K' or self.name == 'P':
            return self.apply_single_discount_offer()
        
        # Check for discount needed to item F - 2F get one F free
        if self.name == 'F' or self.name == 'U':
            return self.apply_get_one_free()
        
        total = self.count*self.price
        return total





