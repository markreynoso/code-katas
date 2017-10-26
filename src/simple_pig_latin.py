"""Kata: Simple Pig Latin.

#1 Best Practices Solution by dykchui, alpharam,
pomps, enfrightened, Wild_Pointer

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if
    word.isalpha() else word for word in lst])
"""


def pig_it(text):
    """Move 1st letter of word to end, add 'ay' to it."""
    text_l = text.split()
    output = []
    pyg = 'ay'
    for word in text_l:
        if word.isalpha():
            first = word[0]
            new_word = word + first + pyg
            new_word = new_word[1: len(new_word)]
            output.append(new_word)
        else:
            output.append(word)
    return ' '.join(output)
