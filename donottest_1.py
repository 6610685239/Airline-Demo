import unittest

from is_prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Test 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Test 2 is prime"""
        self.assertTrue(is_prime(2))

    def test_25(self):
        """Test 25 is not prime"""
        self.assertFalse(is_prime(25))

if __name__ == "__main__":
    unittest.main()