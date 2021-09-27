from typing import TypeVar
import math

Numeric = TypeVar('Numeric', int, float, complex)

def exp(z: Numeric) -> Numeric:
    """Complex exponential function using math.exp
    AZEXP subroutine ported from FORTRAN 77.
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


def arg(number: complex) -> float:
    """Calculate arg function of a complex number."""
    return math.atan2(number.imag, number.real)


def ln(z: Numeric) -> Numeric:
    """Complex natural logarithm using math.log"""
    result = complex(math.log(abs(z)), arg(z))
    if not result.imag:
        if int(result.real) == result.real:
            return int(result.real)
        else:
            return result.real
    return result


if __name__ == '__main__':
    pass
