from solutions.HLO import hello_solution

class TestHello():
    def test_hello(self):
        name = "matty"
        
        result = hello_solution.hello(name)
        assert isinstance(result, str)
        assert name in result