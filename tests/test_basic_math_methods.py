#%%
import unittest
from functions.basic_math import Basic_Math
import math


class TestBasicMath(unittest.TestCase):
    """
        A set of tests for testing Basic_Math methods
    """

    def testExponentNumber(self):
        """
        A method to make an exponentialized number 
        """        
        number = 2
        assert math.sqrt(Basic_Math.exponentNumber(2, number)) == math.sqrt(number)


if __name__ == "__main__":
    unittest.main()