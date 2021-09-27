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
    assert exp.ln(1) == cmath.log(1)
    assert exp.ln(math.e) == 1
    assert exp.ln(2+3j) == cmath.log(2+3j)
    assert exp.arg(2+3j) == cmath.phase(2+3j)
    assert exp.arg(-1) == cmath.phase(-1)
    assert exp.arg(1+1j) == math.pi/4
    assert exp.arg(1j) == math.pi/2
    assert exp.arg(-1j) == -math.pi/2
