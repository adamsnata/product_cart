"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product и его наследников
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(10) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        product.buy(10)
        assert product.quantity == 990

        product.buy(product.quantity)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}
        cart.add_product(product, 10)
        assert cart.products == {product: 20}

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert cart.products == {}

        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert cart.products == {product: 5}

        cart.remove_product(product, 5)
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == product.price * 10

        cart.add_product(product, 10)
        assert cart.get_total_price() == product.price * 20

    def test_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert cart.products == {}

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert cart.products == {}
        assert product.quantity == 990

    def test_buy_with_error(self, cart, product):
        cart.add_product(product, 1010)
        with pytest.raises(ValueError):
            cart.buy()
