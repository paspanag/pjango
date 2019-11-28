import numbers
from math import sqrt


class WeirdComplexNumber(object):
    def __init__(self, real, imag):
        assert isinstance(real, numbers.Number)
        assert isinstance(imag, numbers.Number)

        self._real = real
        self._imag = imag

    def __abs__(self):
        return sqrt(self._real ** 2 + self._imag ** 2)

    def __add__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, numbers.Number):
            return WeirdComplexNumber(self._real + other, self._imag)

        return WeirdComplexNumber(self._real + other._real, self._imag + other._imag)

    def __sub__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, numbers.Number):
            return WeirdComplexNumber(self._real - other, self._imag)

        return WeirdComplexNumber(self._real - other._real, self._imag - other._imag)

    def __mul__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, numbers.Number):
            self._real *= other
            return WeirdComplexNumber(self._real + other, self._imag)

        if isinstance(other, WeirdComplexNumber):
            # x=a+ib and y=c+id
            # (a+ib)(c+id)
            # (ac-bd) + i(ad+bc).

            real = (self._real * other._real) - (self._imag * other._imag)
            imag = (self._real * other._imag) + (self._imag * other._real)
            return WeirdComplexNumber(real, imag)

        return self

    def __eq__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, WeirdComplexNumber):
            other = abs(other)

        return abs(self) == other

    def __lt__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, WeirdComplexNumber):
            other = abs(other)

        return abs(self) < other

    def __gt__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, WeirdComplexNumber):
            other = abs(other)

        return other < abs(self)

    def __le__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, WeirdComplexNumber):
            other = abs(other)

        return abs(self) <= other

    def __ge__(self, other):
        assert isinstance(other, numbers.Number) or isinstance(other, WeirdComplexNumber)

        if isinstance(other, WeirdComplexNumber):
            other = abs(other)

        return other <= (self)

    def __str__(self):
        if self._imag:
            operator = '+' if 0 <= self._imag else '-'
            return f'{self._real} {operator} {abs(self._imag)}i'

        return str(self._real)


print(1 < WeirdComplexNumber(1, 2))
print(WeirdComplexNumber(1, 2) < 5)
print(WeirdComplexNumber(5, 0) == 5)
print(WeirdComplexNumber(8, 0) == WeirdComplexNumber(0, 8))
print(WeirdComplexNumber(8, 0) < WeirdComplexNumber(0, 8))
print(WeirdComplexNumber(8, 0) > WeirdComplexNumber(0, 8))
print(WeirdComplexNumber(0, 8))
print(WeirdComplexNumber(1, 2))
print(WeirdComplexNumber(1, 0))
print(WeirdComplexNumber(1, 0) + WeirdComplexNumber(1, 2))
print(WeirdComplexNumber(2, 1) - WeirdComplexNumber(1, 2))
print(WeirdComplexNumber(2, 1) - WeirdComplexNumber(0, 2))
print(WeirdComplexNumber(2, 1) * WeirdComplexNumber(0, 2))
print(WeirdComplexNumber(2, 1) * WeirdComplexNumber(2, 1))
print(WeirdComplexNumber(2, 1) - 1)
print(WeirdComplexNumber(2, 1) + 1)
