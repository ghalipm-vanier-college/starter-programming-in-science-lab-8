# DO NOT CHANGE THIS FILE, OR ZERO MARK WILL BE ASSIGNED.
import unittest
from Lab8 import dot_product, is_orthogonal


# Test for dot_product()
def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([2, 0, -1], [3, 4, 5]) == 1
    assert dot_product([0, 0, 0], [4, 5, 6]) == 0
    assert dot_product([5], [7]) == 35


# Test for is_orthogonal()
def test_is_orthogonal():
    assert is_orthogonal([1, 2], [-2, 1]) == True     # perpendicular
    assert is_orthogonal([2, 3], [4, 5]) == False     # not perpendicular
    assert is_orthogonal([0, 0], [1, 2]) == False     # zero vector → not valid orthogonal
    assert is_orthogonal([3, -3], [3, 3]) == True 
