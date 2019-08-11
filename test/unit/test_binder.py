#!/usr/local/bin/python3

import pytest

from binder import setup

def test_base_26():
    # Given
    letters = 'abc'

    # When
    x = setup.base_26_characters_to_base_10(letters)

    # Then
    assert x == 730
