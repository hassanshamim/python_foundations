"""
This file contains both successful and failing doctests.
"""


def reverse_words(text):
    """
    >>> reverse_words('Happy Birthday to you')
    'you to Birthday Happy'

    >>> reverse_words('Single')
    'Single'
    """
    words = text.split()
    return ' '.join(reversed(words))


def add(x, y):
    """
    Equivalent to the '+' operator.  Returns the total of two numbers.

    >>> add(1, 3)
    4

    >>> add(-4, 10)
    6
    """
    return x + y


def divide(x, y): # This one fails
    """
    This one fails

    >>> divide(10, 2)
    5

    >>> divide(4, 8)
    0.5

    >>> divide(3, 0)
    Traceback (most recent call last):
    File "..."
    ZeroDivisionError: division by zero
    """
    return x - y


class Pony:
    """
    Classes can include doctests as well
    """

    def __init__(self, name):
        """
        All ponies deserve a name.

        >>> sally = Pony('Sally')
        >>> sally.name
        'Sally'

        >>> another = Pony('Gustoff')
        >>> another.name
        'Gustoff'

        """
        self.name = name

    def is_horse(self):  # Expecting this test to fail
        """

        >>> x = Pony('blah')
        >>> x.is_horse()
        False

        >>> Pony('tim').is_horse()
        True
        """

        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
