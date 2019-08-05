
# -*- coding: utf-8 -*-
import re

from django.conf import settings
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

# convierte las key en minusculas ya que alguana vienen con capital letters
def lower_keys(dictionary):
    if isinstance(dictionary, list):
        return [lower_keys(v) for v in dictionary]
    elif isinstance(dictionary, dict):
        return dict((k.strip().lower(), lower_keys(v)) for k, v in dictionary.iteritems())
    else:
        return dictionary


class BaseConectionTest(TestCase):
    """
        Clase utilizada para la conección al api
        utiliza test_settings para las configuración
    """
    id_session = ''
    username = settings.TEST_USER['username']
    password = settings.TEST_USER['password']
    client = Client()

    def setUp(self):
        self.request = self.client.post(reverse('usercfg:login'),
                                        {'username': self.username, 'password': self.password})
        self.session_id = self.request.url.split('s=')[1]

    def tearDown(self):
        self.client.logout()


class FaresTest(BaseConectionTest):
    def setUp(self):
        super(FaresTest, self).setUp()

    def _request(self, data, url):
        if url == '':
            url = '/prueba/'

        response = self.client.get(url, data)

        respuesta = response.content
        respuesta_recibida = respuesta

        return respuesta_recibida, response.status_code

    def _test_index(self):
        response = self.client.get('/prueba/index/')
        self.assertEqual(200, response.status_code)

    def test_fares(self):
        self._test_index()


    def __parse_qualifiers(self, qualifiers_string):
        patterns = [
            # Taxes. Catches only [Code] or [2 Decimal Amount][Code]. [Integer Amount] may be required
            #u'WS*TX+100YQ'
            r'\*OB\+(?P<ob_fee_amount>(\d+(\.[0-9]{1,2})*))(?P<ob_fee_code>(T|F){1}([0-9]){2})(?P<ob_fee_name>,[a-zA-Z0-9]+)*',
            r'\*(?P<exchange>FEX)',
            r'\*(?P<taxes_exempt>TXEX)',
            r'\*TX(?P<taxes_override>(\d+([0-9])*)*[a-zA-Z](\/?(\d+([0-9])*)*[a-zA-Z]?)+)',
            r'\*TX-(?P<taxes_remove>(\d+([0-9])*)*[a-zA-Z](\/?(\d+([0-9])*)*[a-zA-Z]?)+)',
            #r'\*TX\+(?P<taxes_add>(\d+(\.[0-9]{2})*)*[a-zA-Z]{2}(\/(\d+(\.[0-9]{2})*)*[a-zA-Z]{2})*)(\/-(?P<taxes_remove_while_adding>[a-zA-Z]{2}))*',
            r'\*TX\+(?P<taxes_add>(\d+([0-9])*)*[a-zA-Z](\/?(\d+([0-9])*)*[a-zA-Z]?)+)-?(?P<taxes_remove_while_adding>(([0-9]+)*[a-zA-Z]+)+)?',
            #r'\*TX\+(?P<taxes_add>(\d+\.[0-9]{2})*[a-zA-Z]{2}(\/(\d+\.[0-9]{2})*[a-zA-Z]{2})*)',
            # Base fare and discounts. Need further changes
            r'\*Q(?P<fare_base_alone>\w+)$',
            r'\*Q(?P<fare_base>\w+)*\/(?P<discount_code>[a-zA-Z0-9]*)\/DP(?P<discount_percentage>\d+)(?P<ignore_others>X)*',
            # Charges. Catches only [2 Decimal Amount]. [Integer Amount] may be required
            r'\*CQ(?P<add_charge>([0-9]+,[0-9]{2}|\d+))',
            r'\*(?P<remove_charge>CQEX)',
            r'\*R(?P<origin>[A-Z]{3})',
            r'\*S(?P<segments>[0-9]{1,2}(,[0-9]{1,2})*)',
            r'\*N(?P<passengers>[0-9]{1,2}(,[0-9]{1,2})*)',
            r'\*KP(?P<commission>[0-9]{1,2})',
            r'\*(?P<negotiated_private_rate>NF)',
            #u'WS*D27APR'
            r'\*D(?P<future_date>([0-9]{1,2}[a-zA-Z]{3}))',
            r'\*P(?P<passengers_type>(ADT|CHD|INF)\d{1,2}(\.(ADT|CHD|INF)\d{1,2})*)',
            r'\/(?P<currency>[A-Z]{3})$'
        ]
        joined_patterns_string = '|'.join(patterns)
        pattern = re.compile(joined_patterns_string)
        raw_qualifiers = {}


        for m in pattern.finditer(qualifiers_string):
            raw_qualifiers.update({k: v for k, v in m.groupdict().items() if v})
        qualifiers = self.__format_qualifiers(raw_qualifiers)