'''
Created on Mar 12, 2024

@author: student
'''
import unittest
from main.python import function4Unit2PyTest

class Test(unittest.TestCase):

    def test_factorial(self):
        assert function4Unit2PyTest.factorial(5) == 120

    def test_is_leap_year(self):
        assert function4Unit2PyTest.is_leap_year(2002) == False

'''if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''