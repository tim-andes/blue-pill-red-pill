import unittest

# test array
# test that elements are 0 or 1
# test that elements are type(int) and not floats w/ decimals

class TestArray(unittest.TestCase):
    """
    Tests for arithmetic.
    """
    def test_generate_array(self):
        """
        Tests the `generate_array` function.
        - Check type(array)
        - Check that elements are type(int)
        - Check len(array) is 10,000

        """
        # self.assertEqual(add(2,3), 5)

class TestRandomNumberGenerator(unittest.TestCase):
    """
    Tests random
    """
    def test_generate_zero_one(self):
        """
        Tests the `generate_zero_one` function.
        - Check that all numbers are type(int)
        - Check that all numbers are either 0 or 1
        """
        # self.assertEqual(add(2,3), 5)

# test percentage calculation
class TestCalculateBluePercentage(unittest.TestCase):
    """
    Tests random
    """
    def test_calculate_percent_blue(self):
        """
        Tests the `calculate_percent_blue` function.
        - 
        - Check that all numbers are either 0 or 1
        """
        # self.assertEqual(add(2,3), 5)
# percentage will be int during count

# test output
# percentage will convert to float with two decimal places
# test output red or blue