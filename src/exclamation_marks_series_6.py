"""Kata: Exclamation marks series #6: Remove n exclamation marks in the 
sentence from left to right.

#1 Best Practices Solution by MiraliN, RuiCatela, Demon Slayer, Mr.Child, 
kevin.du, mkosowsk (plus 186 more warriors)

def remove(s, n):
    return s.replace("!", "", n)
"""


def remove(s, n):
    """this function removes n exclamation marks from s"""
    return s.replace('!', '', n)