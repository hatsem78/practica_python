from collections import defaultdict
import collections
from pprint import pprint
from itertools import groupby
from datetime import datetime


class PivoteDict:

    __datetime_format = '%b-%y'
    __data = []
    __group_by = []
    __list_result = []
    __order = ""
    __pivot = ''

    def __init__(self, data_info, group_by_info, date_format=None, order_list=None, field_order=None, pivot=None):
        self.__data = data_info
        self.__group_by = group_by_info
        self.__datetime_format =  '%b-%y'  if date_format is None else date_format
        self.__order = order_list
        self._field_order = field_order
        self.__pivot = pivot

    def order_list(self, group_by, lista):
        order_list = []

        for elemento in lista:
            order_list.insert(self.__order.index(elemento['name_media'].lower()), elemento['value'])
        date1 = datetime.strptime(group_by, "%Y-%m-%dT%H:%M:%SZ").strftime(self.__datetime_format)
        order_list.insert(0, date1)

        return order_list

    def group_by_list(self):

        grouped = collections.defaultdict(list)

        for item in self.__data:
             grouped[item[self.__group_by]].append(item)

        for model, group in grouped.items():
            self.__order.index(item[self._field_order].lower())
            self.__list_result.append(self.order_list(model, group))

    def result(self):
        self.group_by_list()
        return self.__list_result




data = [
    {
        "date": "2017-01-01T00:00:00Z",
        "value": 1252017080.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-01-01T00:00:00Z",
        "value": 235934234.8,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-01-01T00:00:00Z",
        "value": 248418000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-01-01T00:00:00Z",
        "value": 153207.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-02-01T00:00:00Z",
        "value": 132189.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-02-01T00:00:00Z",
        "value": 518912770.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-02-01T00:00:00Z",
        "value": 724232931.1,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-02-01T00:00:00Z",
        "value": 275822000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-03-01T00:00:00Z",
        "value": 126819.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-03-01T00:00:00Z",
        "value": 314261720.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-03-01T00:00:00Z",
        "value": 294243260.1,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-03-01T00:00:00Z",
        "value": 256352000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-04-01T00:00:00Z",
        "value": 432560930.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-04-01T00:00:00Z",
        "value": 168172000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-04-01T00:00:00Z",
        "value": 267588432.9,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-04-01T00:00:00Z",
        "value": 117306.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-05-01T00:00:00Z",
        "value": 166463.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-05-01T00:00:00Z",
        "value": 476015540.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-05-01T00:00:00Z",
        "value": 441642381.4,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-05-01T00:00:00Z",
        "value": 195183000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-06-01T00:00:00Z",
        "value": 138240.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-06-01T00:00:00Z",
        "value": 810101762.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-06-01T00:00:00Z",
        "value": 357835663.2,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-06-01T00:00:00Z",
        "value": 500545000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-07-01T00:00:00Z",
        "value": 1490005960.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-07-01T00:00:00Z",
        "value": 320854000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-07-01T00:00:00Z",
        "value": 432509854.3,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-07-01T00:00:00Z",
        "value": 162686.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-08-01T00:00:00Z",
        "value": 644408580.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-08-01T00:00:00Z",
        "value": 352380400.0,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-08-01T00:00:00Z",
        "value": 181630000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-08-01T00:00:00Z",
        "value": 124474.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-09-01T00:00:00Z",
        "value": 136745.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-09-01T00:00:00Z",
        "value": 240473060.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-09-01T00:00:00Z",
        "value": 517039600.9,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-09-01T00:00:00Z",
        "value": 149401000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-10-01T00:00:00Z",
        "value": 415527992.5,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-10-01T00:00:00Z",
        "value": 173634000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-10-01T00:00:00Z",
        "value": 438218850.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-10-01T00:00:00Z",
        "value": 163267.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-11-01T00:00:00Z",
        "value": 117719.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-11-01T00:00:00Z",
        "value": 642971100.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-11-01T00:00:00Z",
        "value": 486422906.9,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-11-01T00:00:00Z",
        "value": 254729000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2017-12-01T00:00:00Z",
        "value": 168356.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2017-12-01T00:00:00Z",
        "value": 598720550.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2017-12-01T00:00:00Z",
        "value": 740306642.1,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2017-12-01T00:00:00Z",
        "value": 263706000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-01-01T00:00:00Z",
        "value": 186131000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-01-01T00:00:00Z",
        "value": 139820.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-01-01T00:00:00Z",
        "value": 509993060.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-01-01T00:00:00Z",
        "value": 273166325.0,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-02-01T00:00:00Z",
        "value": 1518628960.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-02-01T00:00:00Z",
        "value": 397782973.2,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-02-01T00:00:00Z",
        "value": 333400000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-02-01T00:00:00Z",
        "value": 133758.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-03-01T00:00:00Z",
        "value": 128649.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-03-01T00:00:00Z",
        "value": 1384697520.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-03-01T00:00:00Z",
        "value": 211444616.9,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-03-01T00:00:00Z",
        "value": 197895000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-04-01T00:00:00Z",
        "value": 316200000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-04-01T00:00:00Z",
        "value": 786722472.2,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-04-01T00:00:00Z",
        "value": 710005804.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-04-01T00:00:00Z",
        "value": 195325.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-05-01T00:00:00Z",
        "value": 160757.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-05-01T00:00:00Z",
        "value": 428082433.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-05-01T00:00:00Z",
        "value": 672231948.9,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-05-01T00:00:00Z",
        "value": 183473000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-06-01T00:00:00Z",
        "value": 154042.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-06-01T00:00:00Z",
        "value": 814315030.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-06-01T00:00:00Z",
        "value": 664395048.1,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-06-01T00:00:00Z",
        "value": 208854000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-07-01T00:00:00Z",
        "value": 221526000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-07-01T00:00:00Z",
        "value": 388028778.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-07-01T00:00:00Z",
        "value": 186123.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-07-01T00:00:00Z",
        "value": 735734041.1,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-08-01T00:00:00Z",
        "value": 140139.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-08-01T00:00:00Z",
        "value": 189678041.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-08-01T00:00:00Z",
        "value": 309405008.4,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-08-01T00:00:00Z",
        "value": 137751000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-09-01T00:00:00Z",
        "value": 141347.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-09-01T00:00:00Z",
        "value": 1047967008.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-09-01T00:00:00Z",
        "value": 435554281.2,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-09-01T00:00:00Z",
        "value": 136042000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-10-01T00:00:00Z",
        "value": 1445901540.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-10-01T00:00:00Z",
        "value": 490388000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-10-01T00:00:00Z",
        "value": 595474374.4,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-10-01T00:00:00Z",
        "value": 174419.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-11-01T00:00:00Z",
        "value": 135495.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-11-01T00:00:00Z",
        "value": 518409798.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-11-01T00:00:00Z",
        "value": 937993944.3,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-11-01T00:00:00Z",
        "value": 207217000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    },
    {
        "date": "2018-12-01T00:00:00Z",
        "value": 167024.0,
        "media_id": 3,
        "id_media": 3,
        "name_media": "SALES"
    },
    {
        "date": "2018-12-01T00:00:00Z",
        "value": 1287548696.0,
        "media_id": 1,
        "id_media": 1,
        "name_media": "TV"
    },
    {
        "date": "2018-12-01T00:00:00Z",
        "value": 384209966.0,
        "media_id": 4,
        "id_media": 4,
        "name_media": "INTERNET"
    },
    {
        "date": "2018-12-01T00:00:00Z",
        "value": 359840000.0,
        "media_id": 2,
        "id_media": 2,
        "name_media": "RADIO"
    }
]
columns = ['sales', 'tv', 'internet', 'radio']
lista = PivoteDict(data, 'date', '%b%Y', columns, 'name_media', 'value')
pprint(lista.result())
