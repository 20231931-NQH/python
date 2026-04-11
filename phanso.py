from fractions import Fraction


def normalize_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator == 0:
        raise ValueError('Mẫu số không được bằng 0')
    frac = Fraction(numerator, denominator)
    return frac.numerator, frac.denominator


def cong(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    a, b = frac1
    c, d = frac2
    result = Fraction(a, b) + Fraction(c, d)
    return result.numerator, result.denominator


def tru(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    a, b = frac1
    c, d = frac2
    result = Fraction(a, b) - Fraction(c, d)
    return result.numerator, result.denominator


def nhan(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    a, b = frac1
    c, d = frac2
    result = Fraction(a, b) * Fraction(c, d)
    return result.numerator, result.denominator


def chia(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    a, b = frac1
    c, d = frac2
    if c == 0:
        raise ValueError('Không thể chia cho phân số bằng 0')
    result = Fraction(a, b) / Fraction(c, d)
    return result.numerator, result.denominator
