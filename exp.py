from typing import TypeVar
import math

Numeric = TypeVar('Numeric', int, float, complex)

def exp(z: Numeric) -> Numeric:
    """Complex exponential function using math.exp
    AZEXP ported from FORTRAN 77.
    SUBROUTINE AZEXP(AR, AI, BR, BI)
    C***BEGIN PROLOGUE  AZEXP
    C***REFER TO  ZBESH,ZBESI,ZBESJ,ZBESK,ZBESY,ZAIRY,ZBIRY
    C
    C     DOUBLE PRECISION COMPLEX EXPONENTIAL FUNCTION B=EXP(A)
    C
    C***ROUTINES CALLED  (NONE)
    C***END PROLOGUE  AZEXP
      DOUBLE PRECISION AR, AI, BR, BI, ZM, CA, CB
      ZM = DEXP(AR)
      CA = ZM*DCOS(AI)
      CB = ZM*DSIN(AI)
      BR = CA
      BI = CB
      RETURN
      END
    """
    result = complex(math.exp(z.real)*math.cos(z.imag), math.exp(z.real)*math.sin(z.imag))
    if not result.imag:
        if int(result.real) == result.real:
            return int(result.real)
        else:
            return result.real
    return result


if __name__ == '__main__':
    print(exp(1j))
    print(exp(2+3j), math.exp(2)*exp(3j))
    print(exp(2-3j), math.exp(2)*exp(-3j))
    print(exp(-2+3j), math.exp(-2)*exp(3j))
    print(exp(-2-3j), math.exp(-2)*exp(-3j))
    print(exp(1))
    print(exp(0))
    print(exp(-1))
    print(exp(math.inf))
    print(exp(-math.inf))
    
    import cmath

    print(cmath.exp(1j))
    print(cmath.exp(2+3j))
    print(cmath.exp(2-3j))
    print(cmath.exp(-2+3j))
    print(cmath.exp(-2-3j))
    
