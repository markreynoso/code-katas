"""Assess parenthesis in string."""
from linked_list import LinkedList


def proper_parenthetics(string):
    """Assess parenthesis in string."""
    if not isinstance(string, str):
        raise TypeError('Please enter a unicode string.')
    char_list = LinkedList()
    for letter in string:
        char_list.push(letter)
    count = 0
    total = 0
    current = char_list.head
    while current:
        if current.data == '(':
            count -= 1
            total += 1
            if count < 0:
                return -1
        elif current.data == ')':
            count += 1
            total += 1
        current = current.next
    if total == 0:
        return 'There are no parenthesis in this string.'
    elif count > 0:
        return 1
    else:
        return 0
