import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_1():
    return Item('book', 100.0, 5)


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 7, 2)


def test_item_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 500


def test_item_apply_discount(item_1):
    item_1.pay_rate = 0.5
    item_1.apply_discount()
    assert item_1.calculate_total_price() == 250.0


def test_name_setter(item_1):
    item_1.name = 'Смартфон'
    assert item_1.name == 'Смартфон'
    item_1.name = 'СмартфонСупер'
    assert item_1.name == 'СмартфонСу'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item_1):
    assert repr(item_1) == "Item('book', 100.0, 5)"


def test_str(item_1):
    assert str(item_1) == 'book'


def test_add(item_1, phone_1):
    assert item_1 + item_1 == 10
    assert item_1 + phone_1 == 12
    assert phone_1 + phone_1 == 14
