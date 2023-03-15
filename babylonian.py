"""
~ Babylonian method

@author: Драган Ћајић
@datetime: 10:15 PM Sunday, March 12, 2023
@description:
    Heron's method or Babylonian method for calculating square root of integer.
    precision: 5-digits (epsilon = 10 ^ {-5})
"""
import math

EPSILON = 0.00001


def find_square_root(s, x0):
    xn = x0
    counter = 0

    while True:
        temp_xi = xn
        print("starting value xn =", xn)
        xn = (xn + (s / xn)) / 2
        print("current value xn =", xn)
        print("actual |xn - temp_xi| =", math.fabs(xn - temp_xi))
        counter = counter + 1
        print("end of iteration no.:", counter)
        print("~-" * 20)

        if math.fabs(xn - temp_xi) <= EPSILON:
            break

    return xn
