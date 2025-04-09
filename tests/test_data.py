"""
Tests data.py
"""

from unittest import TestCase
from data import get_population

class Test(TestCase):
    def test_not_empty_dict(self):
        pop = get_population()
        # ensure that no error occured; if an error occured, get_population() would return an empty dictionary
        assert not pop == {}