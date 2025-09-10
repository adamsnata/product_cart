class Product:
    """
    Класс продукта без реализации методов
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity):
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Not enough products')

    def __hash__(self):
        return hash(self.name + self.description)


class ProductByWeight(Product):
    """
    Класс продукта, который продается весом.
    # TODO реализуйте методы
    """
    def check_quantity(self, quantity):
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Not enough products')


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        self.products[product] = self.products.get(product, 0) + quantity

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if quantity is None or quantity >= self.products[product]:
            self.products.pop(product)
        else:
            self.products[product] -= quantity

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        return sum([product.price * quantity for product, quantity in self.products.items()])

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.products.items():
            product.buy(quantity)  #  *****************  тут пробросится исключение , если не будет хватать товара на складе
        self.clear()
