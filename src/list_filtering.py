"""Kata: List Filtering.

#1 Best Practices Solution by clawtros, jtcromwell,
colbydauph, canibanoglu, bilderbuchi, kasterma (plus 86 more warriors)

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
"""


def filter_list(l):
    """Remove all values from list which are not integers."""
    new_l = list(filter(lambda x: type(x) == int, l))
    return new_l
