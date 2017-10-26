"""Kata: Multiples of 3 and 5.

#1 Best Practices Solution by Process, zyxwhut, lowicz, simpajj,
benjaminfigueiredo, nueks (plus 79 more warriors)

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(number):
    """Sum of multiples of 3 or 5 in list."""
    output = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            output = output + i
    return output
