import unittest

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Ensure the test suite can import our module
        """
        try:
            import pymem
        except ImportError:
            self.fail("Was not able to import the emailgraph")

    def test_string(self):
    	from pymem import deep_getsizeof
    	x = '1234567'
    	assert (deep_getsizeof(x, set()) == 44)

if __name__ == "__main__":
    unittest.main()