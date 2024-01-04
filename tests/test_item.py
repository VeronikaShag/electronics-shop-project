import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item_1():
    return Item('book', 100.0, 5)


def test_item_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 500

def test_item_apply_discount(item_1):
    item_1.pay_rate = 0.5
    item_1.apply_discount()
    assert item_1.calculate_total_price() == 250.0
