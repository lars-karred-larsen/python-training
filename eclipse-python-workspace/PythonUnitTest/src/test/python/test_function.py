'''
Created on Mar 8, 2024

@author: student
'''
import unittest
from main.python import function

class Test(unittest.TestCase):


    def test_function(self):
        self.assertEqual(function.validate_marrks(70), "Passed")
        self.assertEqual(function.validate_marrks(40), "Not passed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_function']
    unittest.main()