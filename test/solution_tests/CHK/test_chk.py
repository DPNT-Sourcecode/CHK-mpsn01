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
        pass
        
class TestCheckoutClass():
    def test_init(self):
        skus = "AAA"
        checkout = checkout_solution.Checkout(skus)
        
        assert checkout.receipt == {}
        assert checkout.items == {'A':50, 'B':30, 'C':20, 'D':15}
        
    def test_add_item(self):
        pass
    def test_remove_item(self):
        pass
    def test_total(self):
        pass
    
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
        