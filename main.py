import threading
import random
from enum import Enum
from time import sleep


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
    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index


class TRK:
    trk_status: TrkStatus  # Статус ТРК

    def __init__(self, name: str, grades: list[Grade]):
        self.name = name  # Название ТРК
        self.grades = grades  # Список пистолетов
        self.trk_status = TrkStatus.NOT_READY
        self.dose: int = 0  # Доза на ТРК в мл.


class ServerSocket(threading.Thread):
    list_trk = list[TRK]
    is_running = True

    def __init__(self, ip: str = '127.0.0.1', port: int = 4310):
        super().__init__()
        self.ip = ip  # ip адрес сервера
        self.port = port  # порт сервера

        self.list_trk = [
            TRK('ТРК 1', [Grade('АИ-92', 1), Grade('АИ-95', 2), Grade('ДТ', 3)]),
            TRK('ТРК 2', [Grade('АИ-92', 1), Grade('АИ-95', 2), Grade('ДТ', 3)]),
            TRK('ТРК 3', [Grade('АИ-92', 1), Grade('АИ-95', 2), Grade('ДТ', 3)]),
        ]

    def _update_all_trk(self):
        for trk in self.list_trk:
            trk.trk_status = random.choice(list(TrkStatus))

    def close(self):
        self.is_running = False

    def run(self):
        while self.is_running:
            sleep(1)
            self._update_all_trk()


if __name__ == '__main__':
    ss = ServerSocket()
