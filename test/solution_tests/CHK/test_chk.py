from solutions.CHK import checkout_solution


class TestRunCheckout():
    def test_checkout_no_input(self):
        # Test case 1 - empty string
        result = checkout_solution.checkout("")
        assert isinstance (result, int)
        assert result == 0
    
    def test_checkout_invalid_skus(self):
        # Test case 1 - f included
        result = checkout_solution.checkout("ADFDE")
        assert isinstance (result, int)
        assert result == -1
        
        # Test case 2 - comma included
        result = checkout_solution.checkout("ADD,")
        assert isinstance (result, int)
        assert result == -1
        
        # Test case 3 - space included
        result = checkout_solution.checkout("A DD")
        assert isinstance (result, int)
        assert result == -1
                
    def test_checkout_prices(self):
        # Test case 1
        skus = ""
        assert checkout_solution.checkout(skus) == 0
        
        # Test case 2
        skus = "A"
        assert checkout_solution.checkout(skus) == 50
        
        # Test case 3
        skus = "B"
        assert checkout_solution.checkout(skus) == 30
        
        # Test case 4
        skus = "C"
        assert checkout_solution.checkout(skus) == 20
        
        # Test case 5
        skus = "D"
        assert checkout_solution.checkout(skus) == 15
        
        # Test case 5
        skus = "E"
        assert checkout_solution.checkout(skus) == 40
        
        # Test case 6
        skus = "AAAB"
        assert checkout_solution.checkout(skus) == 160
        
        # Test case 7
        skus = "AAABB"
        assert checkout_solution.checkout(skus) == 175
        
        # Test case 8
        skus = "AABBB"
        assert checkout_solution.checkout(skus) == 175
        
        # Test case 9
        skus = "ABCD"
        assert checkout_solution.checkout(skus) == 115
        
        # Test case 10
        skus = "AAABBAAABCDE"
        assert checkout_solution.checkout(skus) == 410
        
        # Test case 11
        skus = "EB"
        assert checkout_solution.checkout(skus) == 70
        
        # Test case 12
        skus = "EEB"
        assert checkout_solution.checkout(skus) == 80
        
        # Test case 13
        skus = "EEBB"
        assert checkout_solution.checkout(skus) == 95
        
        # Test case 13
        skus = "EEEBBB"
        assert checkout_solution.checkout(skus) == 165
        
        # Test case 14
        skus = "EEEEBB"
        assert checkout_solution.checkout(skus) == 145
        
        # Test case 15
        skus = "EEBBB"
        assert checkout_solution.checkout(skus) == 125
        
        
class TestCheckoutClass():
    def test_init(self):
        checkout = checkout_solution.Checkout()
        
        assert checkout.receipt == {}
        assert checkout.items == {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
        
    def test_add_item(self):
        checkout = checkout_solution.Checkout()
        checkout.add_item('A')
        assert 'A' in checkout.receipt

    def test_remove_item(self):
        checkout = checkout_solution.Checkout()
        checkout.add_item('A')
        checkout.remove_item('A')
        assert 'A' not in checkout.receipt
        
    def test_get_multi_item_discount(self):
        # Test case 1 - empty receipt
        checkout = checkout_solution.Checkout()
        assert checkout.get_multi_item_discount() == 0
        
        # Test case 2 - no multi item discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 0
        
        # Test case 3 - single multi item discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 30
        
        # Test case 4 - still single multi item discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 30
        
        # Test case 5 - double multi item discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 60
        
        # Test case 6 - still double multi item discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('E')
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 60
        
        # Test case 7 - no Bs present to discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('E')
        checkout.add_item('E')
        assert checkout.get_multi_item_discount() == 0
        
    def test_total(self):
        # Test case 1 - Empty
        checkout = checkout_solution.Checkout()
        assert checkout.total() == 0
        
        # Test case 2 - A
        checkout = checkout_solution.Checkout()
        checkout.add_item('A')      
        assert checkout.total() == 50
        
        # Test case 3 - B
        checkout = checkout_solution.Checkout()
        checkout.add_item('B')
        assert checkout.total() == 30
        
        # Test case 4 - C
        checkout = checkout_solution.Checkout()
        checkout.add_item('C')
        assert checkout.total() == 20
        
        # Test case 5 - D
        checkout = checkout_solution.Checkout()
        checkout.add_item('D')
        assert checkout.total() == 15
        
        # Test case 6 - AAAB
        checkout = checkout_solution.Checkout()
        for _ in range(3):
            checkout.add_item('A')
        checkout.add_item('B')
        assert checkout.total() == 160
        
        # Test case 7 - AAABB
        checkout = checkout_solution.Checkout()
        for _ in range(3):
            checkout.add_item('A')
        for _ in range(2):
            checkout.add_item('B')
        assert checkout.total() == 175
        
        # Test case 8 - AABBB
        checkout = checkout_solution.Checkout()
        for _ in range(2):
            checkout.add_item('A')
        for _ in range(3):
            checkout.add_item('B')
        assert checkout.total() == 175
        
        # Test case 9 - ABCD
        checkout = checkout_solution.Checkout()
        checkout.add_item('A')
        checkout.add_item('B')
        checkout.add_item('C')
        checkout.add_item('D')
        assert checkout.total() == 115
        
        # Test case 10 - AAABBAAABCDE
        checkout = checkout_solution.Checkout()
        for _ in range(3):
            checkout.add_item('A')
        for _ in range(2):
            checkout.add_item('B')
        for _ in range(3):
            checkout.add_item('A')
        checkout.add_item('B')
        checkout.add_item('C')
        checkout.add_item('D')
        checkout.add_item('E')
        assert checkout.total() == 410
    
class TestItemClass():
    def test_init(self):
        item = checkout_solution.Item('A', 50)
        assert item.name == 'A'
        assert item.count == 0
        assert item.price == 50
        
        item = checkout_solution.Item('B', 30)
        assert item.name == 'B'
        assert item.count == 0
        assert item.price == 30
        
        item = checkout_solution.Item('C', 20)
        assert item.name == 'C'
        assert item.count == 0
        assert item.price == 20
        
        item = checkout_solution.Item('D', 15)
        assert item.name == 'D'
        assert item.count == 0
        assert item.price == 15
        
    def test_add_one(self):
        item = checkout_solution.Item('A', 50)
        item.add_one()
        assert item.count == 1

    def test_remove_one(self):
        # Test case 1 - An item was removed
        item = checkout_solution.Item('A', 50)
        item.add_one()
        item.remove_one()
        assert item.count == 0
        
        # Test case 2 - too many items removed
        item = checkout_solution.Item('A', 50)
        item.add_one()
        item.remove_one()
        item.remove_one()
        assert item.count == 0
        
    def test_total(self):
        # Test case 1 - AA
        item = checkout_solution.Item('A', 50)
        for _ in range(2):
            item.add_one()

        assert item.total() == 100
        
        # Test case 2 - AAA
        item = checkout_solution.Item('A', 50)
        for _ in range(3):
            item.add_one()

        assert item.total() == 130
        
        # Test case 3 - AAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(4):
            item.add_one()

        assert item.total() == 180
        
        # Test case 4 - AAAAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(6):
            item.add_one()

        assert item.total() == 260
        
        # Test case 5 - B
        item = checkout_solution.Item('B', 30)
        for _ in range(1):
            item.add_one()

        assert item.total() == 30
        
        # Test case 6 - BB
        item = checkout_solution.Item('B', 30)
        for _ in range(2):
            item.add_one()

        assert item.total() == 45
        
        # Test case 7 - BBB
        item = checkout_solution.Item('B', 30)
        for _ in range(3):
            item.add_one()

        assert item.total() == 75
        
        # Test case 8 - BBBB
        item = checkout_solution.Item('B', 30)
        for _ in range(4):
            item.add_one()

        assert item.total() == 90
        
        # Test case 9 - C
        item = checkout_solution.Item('C', 20)
        item.add_one()
        assert item.total() == 20
        
        # Test case 10 - no items
        item = checkout_solution.Item('A', 20)
        assert item.total() == 0
        

