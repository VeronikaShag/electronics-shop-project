from src.item import Item


class MixinLanguage:


    def __init__(self):
        language = 'EN'
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLanguage):

    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        super().__init__(name, price, quantity)
        self.__language = language
        if self.__language.upper() != "EN" and self.__language.upper() != "RU":
            raise ValueError('Язык клавиатуры может быть только EN или RU')