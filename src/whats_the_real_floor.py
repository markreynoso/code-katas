"""Kata: What's The Real Floor.

#1 Best Practices Solution by catherinebacon, a0Ws8Ypd9HVxf4, ajusNegro

def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2
"""

def get_real_floor(n):
    """returns the actual level of an americanized floor label"""
    if n <= 0:
        return n
    elif n > 0 and n < 13:
        return n - 1
    elif n > 13:
        return n - 2