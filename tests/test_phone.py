import pytest

from src.phone import Phone


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str_repr_phone(phone_1):
    assert str(phone_1) == 'iPhone 14'
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_1.number_of_sim == 2
