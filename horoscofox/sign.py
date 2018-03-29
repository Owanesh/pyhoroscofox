import requests
from datetime import datetime, timedelta

from .constants import URL_ENDPOINT
from .errors import PaoloException
from .response import Response
from random import randint


class Sign():

    def __init__(self, sign):
        self.sign = sign

    def _generic_body(self, kind):
        return {
            "id": str(randint(330000, 9900000)),
            "method": "getContents",
            "params": {
                "config": {
                    "app_uid": "5317e225-47f7-96af8059",
                    "action": kind,
                    "content_provider": "mmdb",
                    "content_type": "text",
                    "service_param": self.sign
                }
            }
        }

    def _generic_request(self, kind):
        try:
            r = requests.post(
                URL_ENDPOINT,
                json=self._generic_body(kind),
            )
            if r.status_code != 200:
                raise PaoloException('Error using API!')
        except requests.exceptions.ConnectionError:
            raise PaoloException('Connection error!')
        json_resp = r.json()
        date_start = datetime.strptime(
            json_resp['result']['elem'][0]['content_date'],
            '%Y-%m-%d  %H:%M:%S'
        )
        date_end = None
        if kind == 'daily':
            date_end = date_start + timedelta(days=1)
        elif kind == 'tomorrow':
            date_end = date_start + timedelta(days=1)

        if date_start:
            date_start = date_start.date()

        if date_end:
            date_end = date_end.date()
        # elif kind == 'monthly':
        #     date_end = date_start + timedelta(days=28)

        return Response(
            json_resp['result']['elem'][0]['text'],
            date_start, date_end
        )

    def today(self):
        return self._generic_request('daily')

    def tomorrow(self):
        return self._generic_request('tomorrow')

    # def week(self):
    #     return self._generic_request('weekly')

    # def month(self):
    #     return self._generic_request('monthly')
