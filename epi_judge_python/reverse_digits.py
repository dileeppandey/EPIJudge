from test_framework import generic_test
from math import log10
from math import floor


def reverse(x):
    # TODO - you fill in here.
    result = 0
    is_negative = False
    if x < 0:
        is_negative = True
    x = abs(x)
    while x > 0:
        result += (10 ** floor(log10(x))) * (x % 10)
        x //= 10
    return result if not is_negative else -1 * result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
