'''
Created on Mar 11, 2024

@author: student
'''
from main.python import markersFunction
import platform
import pytest

@pytest.mark.skip(reason = "Testing skipping a test")
def test_skipping():
    assert False
    
@pytest.mark.skipif(platform.system() == "Linux", reason = "Skipping test for demonstration")
def test_factorial():
    assert markersFunction.factorial(5) == 120
    
@pytest.mark.xfail(reason = "Demonstrating failure")
def test_expected_failure():
    assert False
    
@pytest.mark.parametrize("year, result", [
    (2000, True),
    (2024, True),
    (2025, False),
    (2100, False),
    (2104, True)
    ])

def test_is_leap_year(year, result):
    assert markersFunction.is_leap_year(year) is result