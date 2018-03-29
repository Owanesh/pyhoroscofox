from .constants import SIGNS
from .errors import PaoloException
from .sign import Sign


class PaoloClient():

    def __init__(self):
        super().__init__()
        for sign in SIGNS:
            sign_object = Sign(sign)
            setattr(self, sign, sign_object)

    def get(self, sign, kind):
        sign = getattr(self, sign, None)
        if kind == 'today':
            return sign.today()
        elif kind == 'tomorrow':
            return sign.tomorrow()
        else:
            raise PaoloException()