"""Kata: Sum of Two Lowest Possible Integers.

#1 Best Practices Solution by danman1979, MirzaI,
mstrfx, VadimPopov, dmpage, redundnt (plus 356 more warriors)

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Sum of the two lowest integers in list."""
    num_ord = sorted(numbers)
    return num_ord[0] + num_ord[1]
