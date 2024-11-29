"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """
    Formats the phrase as a sentence.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('today is sunny')
    'Today is sunny.'
    """
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase.capitalize()


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car1 = Car()
    assert test_car1.fuel == 0, "Car default fuel is not set to 0"
    assert test_car1._odometer == 0, "Car does not set odometer correctly"

    test_car2 = Car(fuel=10)
    assert test_car2.fuel == 10, "Car does not set fuel correctly when provided"


run_tests()
doctest.testmod()
