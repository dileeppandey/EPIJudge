from test_framework import generic_test


def count_bits(x: int) -> int:
    return sum([int(ch) for ch in bin(x)[2:]])


def count_bits_bitwise(x: int) -> int:
    count = 0
    while x != 0:
        count = count + 1 if x & 1 == 1 else count
        x = x >> 1
    return count


if __name__ == '__main__':
    generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                   count_bits)
    generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                   count_bits_bitwise)
