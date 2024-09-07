import math_functions

def test_add():
    assert math_functions.add(2, 3) == 5
    assert math_functions.add(-1, 1) == 0
    assert math_functions.add(0, 0) == 0

def test_subtract():
    assert math_functions.subtract(5, 3) == 2
    assert math_functions.subtract(0, 0) == 0
    assert math_functions.subtract(-1, -1) == 0