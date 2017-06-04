import unittest
from pymemory import deep_getsizeof

class InitializationTests(unittest.TestCase):

    def setup(self):
        pass

    def test_integer(self):
        x = 5
        assert(deep_getsizeof(x, set()) == 24)

    def test_float(self):
        x = 5.3
        assert(deep_getsizeof(x, set()) == 24)

    def test_emptystring(self):
        x = ""
        assert(deep_getsizeof(x, set()) == 37)        

    def test_string(self):
        x = "1234567"
        assert(deep_getsizeof(x, set()) == 44)

    def test_emptyunicode(self):
        x = u""
        assert(deep_getsizeof(x, set()) == 50)

    def test_unicodestring(self):
        x = u"1"
        assert(deep_getsizeof(x, set()) == 104)

    def test_emptylist(self):
        x = []
        assert(deep_getsizeof(x, set()) == 72)

if __name__ == "__main__":
    unittest.main()