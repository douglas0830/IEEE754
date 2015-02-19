#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# John Zimmerman
#

class IEEE754(object):

    """
        Converts a IEEE 754 binary number to Base10
    """

    def __init__(self, b):
        self.__b = ''.join(b.split(' '))

    def __to_base10(self, bi):
        return sum([2**i for i,b in enumerate(reversed(bi)) if b=="1"])

    @property
    def mantissa(self):
        return 1 + sum([1.0/(2**(i+1)) for i,b in enumerate(self.__b[9:]) if b=="1"])

    @property
    def signbit(self):
        return (-1)**int(self.__b[0])

    @property
    def exponent(self):
        return 2**(self.__to_base10(self.__b[1:9]) - 127)

    @property
    def base10(self):
        return self.signbit * self.exponent * self.mantissa

    def __str__(self):
        return self.__b


def main():
    iee754 = "0100 1000 0000 1111 1000 1010 1101 1010"
    i = IEEE754(iee754)
    print i
    print i.base10
    print i.signbit
    print i.exponent
    print i.mantissa

    rating = " "
    if isinstance(rating, int):
        print "nope"

if __name__ == '__main__':
    main()
