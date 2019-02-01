"""
Tests the add() function of the calculator.
"""
from calculator import multiply


def test_five_multiply_two():
    """
    If given 5 and 2 as parameters, 10 should
    be returned
    """
    assert multiply(5, 2) == 10

def test_eight_multiply_three():
    assert multiply(8, 3) == 24
    """
    If given 8 and 3 as parameters, 24 should
    be returned
    """

def test_no_parameter():
    """ if no parameters are provided, return 0
    """
