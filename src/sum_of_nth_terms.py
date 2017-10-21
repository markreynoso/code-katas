"""Kata: Sum of nth Terms.

#1 Best Practices Solution by MMMAAANNN, doctornick5, Slx64, ninja37,
FablehavenGeek, nabrarpour4 (plus 17 more warriors)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""

def series_sum(n):
    """returns sum of 1 / denominator which increments by 3 for n
    number of times. result is returned to two decimals places as a string"""
    output = 0
    inc = -2
    for i in range(n):
        inc = inc + 3
        output = output + (1/inc)
        print(output)
    return '%.2f' % output