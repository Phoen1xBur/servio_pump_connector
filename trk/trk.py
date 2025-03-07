from enum import Enum

from sp_const import *


class TrkStatus(Enum):
    # Каждый элемент перечисления содержит три значения: name, description и color
    NOT_CONNECTED = ('Нет соединения с сервером', 'red')
    NOT_READY = ('ТРК недоступна', 'red')
    READY = ('ТРК доступна', 'green')
    INSTALL_DOSE = ('Установлена доза на ТРК', 'yellow')
    OUTPUT_DOSE = ('На ТРК идет отпуск топлива', 'blue')

    # Инициализация дополнительных атрибутов
    def __init__(self, description, color):
        self.description = description  # Основное значение (value)
        self.color = color  # Дополнительный атрибут


class Grade:
    grade_id: int
    kind: int
    item: str
    name: str
    price: float

    __ANALOG_NAME = {
        TAG_FPC_NOZZLE_ID: 'grade_id',
        TAG_FPC_KIND: 'kind',
        TAG_FPC_ITEM: 'item',
        TAG_FPC_NAME: 'name',
        TAG_FPC_PRICE: 'price',
    }

    def __init__(self, *_, **kwargs):
        for key, value in kwargs.items():
            if self.__ANALOG_NAME.get(key):
                setattr(self, self.__ANALOG_NAME[key], value)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class TRK:
    trk_id: int
    status: int
    trans_id: int
    active_grade_id: int
    price: float
    liters: float
    money: float
    kind: str

    trk_status: TrkStatus  # Статус ТРК

    __ANALOG_NAME = {
        TAG_FPS_FUELLINGPOINT_ID: 'trk_id',
        TAG_FPS_STATUS: 'status',
        TAG_FPS_TRANS_ID: 'trans_id',
        TAG_FPS_NOZZLE_ID: 'active_grade_id',
        TAG_FPS_PRICE: 'price',
        TAG_FPS_LITERS: 'liters',
        TAG_FPS_MONEY: 'money',
        TAG_FPS_KIND: 'kind',
    }

    def __init__(self, grades: list[Grade], *_, **kwargs):
        for key, value in kwargs.items():
            if self.__ANALOG_NAME.get(key):
                setattr(self, self.__ANALOG_NAME[key], value)

        self.name = f'ТРК - {self.trk_id}'  # Название ТРК
        self.grades: list[Grade] = grades  # Список пистолетов
        # self.trk_status = TrkStatus.NOT_READY

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}[Grade({self.grades})])'