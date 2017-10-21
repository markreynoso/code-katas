"""Kata: Changing Letters.

#1 Best Practices Solution by ZozoFouchtra, Beast, Unnamed,
siebenschlaefer, FranzSchubert92, AlexBaier (plus 2 more warriors)

def swap(st):
    return "".join( c.upper() if c in "aeiou" else c for c in st )
"""

def swap(st):
    """changes all vowels to uppercase"""
    st_list = list(st)
    vowels = 'aeiou'
    output = []
    for letter in st_list:
        if vowels.find(letter) >= 0:
            output.append(letter.upper())
        else:
            output.append(letter)
    return ''.join(output)