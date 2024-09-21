from solutions.CHK import checkout_solution


class TestRunCheckout():
    def test_checkout_no_input(self):
        # Test case 1 - empty string
        result = checkout_solution.checkout("")
        assert isinstance (result, int)
        assert result == 0
    
    def test_checkout_invalid_skus(self):
        # Test case 1 - % included
        result = checkout_solution.checkout("AD%DE")
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
        assert checkout_solution.checkout(skus) == 400
        
        # Test case 11
        skus = "EB"
        assert checkout_solution.checkout(skus) == 70
        
        # Test case 12
        skus = "EEB"
        assert checkout_solution.checkout(skus) == 80
        
        # Test case 13
        skus = "EEBB"
        assert checkout_solution.checkout(skus) == 110
        
        # Test case 14
        skus = "EEEEB"
        assert checkout_solution.checkout(skus) == 160
        
        # Test case 15
        skus = "EEEEBB"
        assert checkout_solution.checkout(skus) == 160
        
        # Test case 16
        skus = "EEBBB"
        assert checkout_solution.checkout(skus) == 125
        
        # Test case 17
        skus = "AAA"
        assert checkout_solution.checkout(skus) == 130
        
        # Test case 18
        skus = "AAAAA"
        assert checkout_solution.checkout(skus) == 200
        
        # Test case 19
        skus = "AAAAAA"
        assert checkout_solution.checkout(skus) == 250
        
        # Test case 20
        skus = "AAAAAAAA"
        assert checkout_solution.checkout(skus) == 330
        
        # Test case 21
        skus = "AAAAAAAAAA"
        assert checkout_solution.checkout(skus) == 400
        
        
class TestCheckoutClass():
    def test_init(self):
        checkout = checkout_solution.Checkout()
        
        assert checkout.receipt == {}
        assert checkout.items == {
            'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20, 'H':10,
            'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 
            'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90,
            'Z': 50}
        
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
        
        # Test case 8 - 2 Bs present to discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 15
        
        # Test case 9 - 3 Bs present to discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('B')
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 15

        # Test case 10 - 4 Bs present to discount
        checkout = checkout_solution.Checkout()
        checkout.add_item('B')
        checkout.add_item('B')
        checkout.add_item('B')
        checkout.add_item('B')
        assert checkout.get_multi_item_discount() == 30
        
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
        assert checkout.total() == 400
        
        # Test case 11 - AAAAA
        checkout = checkout_solution.Checkout()
        for _ in range(5):
            checkout.add_item('A')
        assert checkout.total() == 200
        
        # Test case 12 - AAAAAAAA
        checkout = checkout_solution.Checkout()
        for _ in range(8):
            checkout.add_item('A')
        assert checkout.total() == 330
        
        # Test case 12 - AAAAAAAA
        checkout = checkout_solution.Checkout()
        for _ in range(10):
            checkout.add_item('A')
        assert checkout.total() == 400
        
        # Test case 12 - AAAAAAAA
        checkout = checkout_solution.Checkout()
        for _ in range(11):
            checkout.add_item('A')
        assert checkout.total() == 450
    
class TestItemClass():
    def test_init(self):
        item = checkout_solution.Item('A', 50)
        assert item.name == 'A'
        assert item.count == 0
        assert item.price == 50
        
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
        
    def test_single_discount_offer(self):
        # Test case 1 - K
        item = checkout_solution.Item('K', 80)
        item.add_one()
        assert item.total() == 80
        
        # Test case 2 - KK
        item = checkout_solution.Item('K', 80)
        item.add_one()
        assert item.total() == 150
        
        # Test case 3 - 3 x K
        item = checkout_solution.Item('K', 80)
        for _ in range(3):
            item.add_one()
        assert item.total() == 230
        
        # Test case 4 - 4 x K
        item = checkout_solution.Item('K', 80)
        for _ in range(4):
            item.add_one()
        assert item.total() == 300
    
    def test_double_discount_offer(self):
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
        
        # Test case 4 - AAAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(5):
            item.add_one()
        assert item.total() == 200
        
        # Test case 4 - AAAAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(6):
            item.add_one()
        assert item.total() == 250
        
        # Test case 4 - AAAAAAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(8):
            item.add_one()
        assert item.total() == 330
        
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
        assert item.total() == 250
        
        # Test case 4 - AAAAAAAA
        item = checkout_solution.Item('A', 50)
        for _ in range(8):
            item.add_one()
        assert item.total() == 330
        
        # Test case 5 - 11 x A
        item = checkout_solution.Item('A', 50)
        for _ in range(11):
            item.add_one()
        assert item.total() == 450
        
        # Test case 5 - 14 x A
        item = checkout_solution.Item('A', 50)
        for _ in range(14):
            item.add_one()
        assert item.total() == 580
        
        # Test case 5 - B
        item = checkout_solution.Item('B', 30)
        for _ in range(1):
            item.add_one()
        assert item.total() == 30
                
        # Test case 9 - C
        item = checkout_solution.Item('C', 20)
        item.add_one()
        assert item.total() == 20
        
        # Test case 10 - no items
        item = checkout_solution.Item('A', 20)
        assert item.total() == 0
        
        # Test case 11 - FF
        item = checkout_solution.Item('F', 10)
        item.add_one()
        item.add_one()
        assert item.total() == 20
        
        # Test case 11 - FFF
        item = checkout_solution.Item('F', 10)
        for _ in range(3):
            item.add_one()
        assert item.total() == 20
        
        # Test case 12 - 5 x F
        item = checkout_solution.Item('F', 10)
        for _ in range(5):
            item.add_one()
        assert item.total() == 40
        
        # Test case 13 - 6 x F
        item = checkout_solution.Item('F', 10)
        for _ in range(6):
            item.add_one()
        assert item.total() == 40
        