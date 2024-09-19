from solutions.HLO import hello_solution

class TestHello():
    def test_hello(self):
        result = hello_solution.hello("matty")
        assert isinstance(result, str)