"""
Tests Population.py
"""

from unittest import TestCase
from streamlit.testing.v1 import AppTest

class Test(TestCase):
    def test_title_and_button(self):
        at = AppTest.from_file("./src/Population.py")
        at.run()

        assert at.title[0].value.startswith("US Population By Year")
        assert at.button[0].label.startswith("Toggle Display Method")
        assert not at.exception