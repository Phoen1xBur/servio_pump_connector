import time
from enum import Enum
from dotenv import dotenv_values

import requests
from sp_const import *
from trk.trk import TRK, Grade


class Method(Enum):
    POST = 'POST'
    GET = 'GET'


class ServioPumpAPI:
    DEVELOPER_CODE = ''
    BASE_URL = ''
    _HOST = ''
    _PORT = ''


    def __init__(self):
        self.config = dotenv_values('.env')

        self._update_params()

        self.BASE_URL = f'{self._HOST}:{self._PORT}/'

    def _update_params(self):
        self.DEVELOPER_CODE = self.config.get('DEVELOPER_CODE', None)
        if self.DEVELOPER_CODE is None:
            raise ValueError('DEVELOPER_CODE environment variable is missing.')
        self._HOST = self.config.get('HOST', 'http://127.0.0.1')
        self._PORT = self.config.get('PORT', 44310)

    @staticmethod
    def _get_params() -> dict:
        unique_id = str(time.time()).replace('.', '')
        params = { TAG_REQUEST_ID: unique_id }
        return params

    def _request(self, method: Method, *_, url_request: str = '', json: dict = None) -> dict:
        """
        Общая структура для каждого запроса
        :param method: Метод запроса Post | Get
        :param url_request: Запрос к конкретному узлу
        :param json: Данные для передачи если такие имеются
        :return: Возвращает тело запроса при успешном status_code
        """
        if json is None:
            json = {TAG_DEVELOPER_CODE: self.DEVELOPER_CODE}

        if json.get(TAG_DEVELOPER_CODE) is None:
            json[TAG_DEVELOPER_CODE] = self.DEVELOPER_CODE

        url = self.BASE_URL + url_request
        params = self._get_params()

        response = requests.request(method.value, url, json=json, params=params)
        if response.status_code != 200:
            raise Exception(response.text)
        try:
            data = response.json()
            return data
        except ValueError:
            raise Exception(response.text)

    def get_grades_by_trk(self, trk_id: int) -> list[Grade]:
        json = {
            TAG_METHOD: METHOD_GET_NOZZLE_CONFIG,
            TAG_FPS_FUELLINGPOINT_ID: trk_id,
        }
        data = self._request(Method.POST, json=json)
        grades: list[Grade] = []
        if data.get(TAG_FPC_NOZZLES) is None:
            return grades
        for grade in data[TAG_FPC_NOZZLES]:
                grades.append(Grade(**grade))

        return grades

    def get_trk_list(self) -> list[TRK]:
        json = {
            TAG_METHOD: METHOD_GET_FUELLING_POINT_STATUS,
        }
        data = self._request(Method.POST, json=json)
        trk_list: list[TRK] = []
        if data.get(TAG_FPC_FUELLINGPOINTS) is None:
            return trk_list

        for trk in data[TAG_FPC_FUELLINGPOINTS]:
            trk: dict
            grades = None
            if trk.get(TAG_FPS_FUELLINGPOINT_ID):
                grades = self.get_grades_by_trk(trk_id=trk[TAG_FPS_FUELLINGPOINT_ID])
            trk_list.append(TRK(grades, **trk))
        return trk_list


if __name__ == '__main__':
    SS = ServioPumpAPI()
    trk_list = SS.get_trk_list()
    print(trk_list)
