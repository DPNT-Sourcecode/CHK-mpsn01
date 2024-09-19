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
        
        assert items == checkout.items
        
    def test_add_item(self):
        pass
    def test_remove_item(self):
        pass
    def test_total(self):
        pass
    
class TestItemClass():
    def test_init(self):
        item = checkout_solution.Item('A')
        assert item.count == 0
        assert item.price == 50
        
        item = checkout_solution.Item('B')
        assert item.count == 0
        assert item.price == 30
        
        item = checkout_solution.Item('C')
        assert item.count == 0
        assert item.price == 30
        
        item = checkout_solution.Item('C')
        assert item.count == 0
        assert item.price == 15
        
    def test_add_one(self):
        pass
    def test_remove_one(self):
        pass
    def test_total(self):
        pass