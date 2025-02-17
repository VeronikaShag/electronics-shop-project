import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        self.__name = name_str[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv_file: str):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        try:
            open(csv_file, 'r', encoding='utf-8')
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        else:
            cls.all = []
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for i in reader:
                    if 'name' not in i or 'price' not in i or 'quantity' not in i:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        cls(i['name'], i['price'], i['quantity'])

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и Phone.')
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    """
    Класс ошибки при отсутствии одной из колонок в файле items
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'
