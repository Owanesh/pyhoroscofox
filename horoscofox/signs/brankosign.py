from .sign import Sign

import requests
from datetime import datetime, timedelta

from horoscofox.constants import BRANKO_URL_ENDPOINT, IT_SIGNS
from horoscofox.errors import AstrologerException
from horoscofox.response import Response


class BrankoSign(Sign):

    def _generic_body(self):
        return {'segno': IT_SIGNS[self.sign].upper()}

    def _generic_request(self, kind):

        try:
            r = requests.get(
                BRANKO_URL_ENDPOINT,
                params=self._generic_body(),
            )
            if r.status_code != 200:
                raise AstrologerException('Error using API!')
        except requests.exceptions.ConnectionError:
            raise AstrologerException('Connection error!')
        json_resp = r.json()
        date_start = datetime.strptime(
            json_resp['oroscopo'][0]['createdAt'],
            '%Y-%m-%d  %H:%M:%S'
        )
        if kind == 'today':
            date_end = date_start + timedelta(days=1)
        
        if date_start:
            date_start = date_start.date()

        if date_end:
            date_end = date_end.date()

        return Response(
            json_resp['oroscopo'][0]['oroscopo'],
            date_start, date_end
        )

    def today(self):
        return self._generic_request('today')
