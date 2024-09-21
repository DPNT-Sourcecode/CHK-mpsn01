

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
            'I':35, 'J':60, 'K':70, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 
            'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90,
            'Y': 10,'Z': 50}
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
            
    def get_multi_item_discount(self, item_x: str, item_y: str) -> int:
        # define eligible items and discounts
        # example: '[[2,15], {'E':2}]' index 1 represents the number of E required to get a
        # free B, index 0 represents the discount available if 2B are purchased.
        discount = 0        
        offers = {'B': [[2,15], {'E':2}], 'M':[[0,0], {'N':3}], 'Q': [[3,10], {'R':3}]}
        
        num_x_items = self.receipt[item_x].count
        
        num_y_items = 0
        if item_y in self.receipt:        
            num_y_items = self.receipt[item_y].count
        
        # check for free item_x discount
        required_num_y = offers[item_x][1][item_y]
        num_y_sets = min(num_y_items // required_num_y, num_x_items)
        num_x_items -= num_y_sets
        discount_y_set = self.items[item_x]
        discount += num_y_sets * discount_y_set
        
        if num_x_items < 0:
            num_x_items = 0
            
        # apply remaining single item discount offer
        if item_x != 'M':
            required_num_x = offers[item_x][0][0]
            num_x_sets = num_x_items // required_num_x
            discount_x_set = offers[item_x][0][1]
            discount += num_x_sets * discount_x_set
        
        return discount
    
    # check_for_discounts is used to search for cross item offers and return
    # the value of the discount to be subtracted from the final bill. 
    def check_for_discounts(self) -> int:
        discount = 0
        
        if len(self.receipt) == 0:
            return 0
        
        if 'B' in self.receipt:
            discount += self.get_multi_item_discount('B', 'E')
            
        if 'M' in self.receipt:
            discount += self.get_multi_item_discount('M', 'N')
            
        if 'Q' in self.receipt:
            discount += self.get_multi_item_discount('Q', 'R')
         
        return discount
            
    def total(self) -> int:
        sum = 0
        for item in self.receipt.values():
            sum = sum + item.total()
            
        return sum - self.check_for_discounts()

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
        items = {'K':[2,120],'P': [5,200]}
        
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
        
        # Check for discounts with multiple offers available
        if self.name == 'A' or self.name == 'H' or self.name == 'V':
            return self.apply_double_discount_offer()
        
        # Check for discounts with a single offer available
        if self.name == 'K' or self.name == 'P':
            return self.apply_single_discount_offer()
        
        # Check for discounts with get one free offers
        if self.name == 'F' or self.name == 'U':
            return self.apply_get_one_free()
        
        total = self.count*self.price
        return total
