"""Kata: Find the Odd Int.

#1 Best Practices Solution by cerealdinner, ynnake, sfr,
netpsychosis, VadimPopov, user7514902 (plus 291 more warriors)

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""

def find_it(seq):
    """returns the integer which occurs an odd numbers of times in list"""
    for item in seq:
        total = seq.count(item)
        if total % 2 == 1:
          return item