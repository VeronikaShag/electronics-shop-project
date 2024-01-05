import codecs
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
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) < 10:
            self.__name = name_str
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
        cls.all = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i in reader:
                cls(i['name'], i['price'], i['quantity'])

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))