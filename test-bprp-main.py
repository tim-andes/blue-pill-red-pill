import unittest
import bprp


# test that elements are 0 or 1
# test that elements are type(int) and not floats w/ decimals
class TestBprp(unittest.TestCase):
    def test_generate_zero_one(self):
        """
        Tests the `generate_zero_one` function.
        - Check that all numbers are type(int)
        - Check that all numbers are either 0 or 1
        """
        self.assertLessEqual(bprp.generate_zero_one(), 1)
        self.assertGreaterEqual(bprp.generate_zero_one(), 0)
        self.assertIsInstance(bprp.generate_zero_one(), int)

    def test_generate_array(self):
        """
        Tests the `generate_array` function.
        - Check type(array)
        - Check len(array) is 10,000
        """
        self.assertIsInstance(bprp.generate_array(), list)
        self.assertEqual(len(bprp.generate_array()), 10000)

    def test_tally(self):
        """
        Tests the `tally` function which outputs a 2 element array, where [# 0's, # 1's]
        - Check type(array)
        - Check that tally array length is 2
        - Check that elements are both type(int)
        """
        self.assertIsInstance(bprp.tally(), list)
        self.assertEqual(len(bprp.tally()), 2)

    def test_percentage(self):
        """
        Tests the `percentage` function.
        - Check type(float)
        - Check that percentage is less than or equal to 1.0
        """     
        self.assertIsInstance(bprp.percentage(), float)
        self.assertLessEqual(bprp.percentage(), 100.00)  
        self.assertGreaterEqual(bprp.percentage(), 0)      

    # def test_calculate_percent_blue(self):
    #     """
    #     Tests the `calculate_percent_blue` function.
    #     - 
    #     - Check that all numbers are either 0 or 1
    #     """
    #     # self.assertEqual(add(2,3), 5)

# percentage will be int during count
# test output
# percentage will convert to float with two decimal places
# test output red or bluetest=

if __name__ == "__main__":
    unittest.main()