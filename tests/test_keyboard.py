import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard_1():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_name_keyboard(keyboard_1):
    assert keyboard_1.name == 'Dark Project KD87A'
    assert keyboard_1.price == 9600
    assert keyboard_1.quantity == 5
    assert str(keyboard_1.language) == "EN"

def test_change_lang(keyboard_1):
    keyboard_1.change_lang()
    assert str(keyboard_1.language) == "RU"
    keyboard_1.change_lang()
    assert str(keyboard_1.language) == "EN"