import cmath
import math

import exp

def test_exp():
    """pytest tests."""
    assert exp.exp(1j) == cmath.exp(1j)
    assert exp.exp(2+3j) == math.exp(2)*exp.exp(3j)
    assert exp.exp(2+3j) == cmath.exp(2+3j)
    assert exp.exp(2-3j) == math.exp(2)*exp.exp(-3j)
    assert exp.exp(2-3j) == cmath.exp(2-3j)
    assert exp.exp(-2+3j) == math.exp(-2)*exp.exp(3j)
    assert exp.exp(-2+3j) == cmath.exp(-2+3j)
    assert exp.exp(-2-3j) == math.exp(-2)*exp.exp(-3j)
    assert exp.exp(-2-3j) == cmath.exp(-2-3j)
    assert exp.exp(1) == cmath.exp(1)
    assert exp.exp(0) == cmath.exp(0)
    assert exp.exp(-1) == cmath.exp(-1)
    #assert exp.exp(math.inf) == cmath.exp(math.inf)
    assert exp.exp(-math.inf) == cmath.exp(-math.inf)
