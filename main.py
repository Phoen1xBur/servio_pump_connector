import threading
import random
from enum import Enum
from time import sleep

from sp_api import ServioPumpAPI
from trk.trk import TRK, Grade, TrkStatus


class ServerSocket(threading.Thread):
    list_trk = list[TRK]
    is_running = True
    SP = ServioPumpAPI()

    def __init__(self):
        super().__init__()

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
