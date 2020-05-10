from test_framework import generic_test


def count_bits(x: int) -> int:
    return sum([int(ch) for ch in bin(x)[2:]])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
