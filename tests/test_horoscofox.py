from datetime import datetime
from horoscofox import paolo


def test_client_today(mocker):
    mock_response = {
        "result": {
            "elem": [
                {
                    "text": "Va tutto male",
                    "short_text": "Bel periodo si",
                    "content_id": "7985824",
                    "content_date": "2018-03-29 00:00:00",
                    "title": "SCORPIONE",
                    "subtitle": "29 Marzo 2018"
                }
            ],
            "datetime": "2018-03-29 00:04:56",
            "timestamp": 1522281896,
            "t_active": "true",
            "t_days": 1,
            "t_frequency_days": 7,
            "ads": "admob",
            "rewarded_video_libs": []
        },
        "id": "5713030"
    }
    mocked_post = mocker.patch('horoscofox.signs.requests.post')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = paolo.scorpio.today()
    assert resp.text == 'Va tutto male'
    assert resp.date_start == datetime(2018, 3, 29, 0, 0).date()
    assert resp.date_end == datetime(2018, 3, 30, 0, 0).date()

    resp = paolo.get(sign='scorpio', kind='today')
    assert resp.text == 'Va tutto male'
    assert resp.date_start == datetime(2018, 3, 29, 0, 0).date()
    assert resp.date_end == datetime(2018, 3, 30, 0, 0).date()


def test_client_tomorrow(mocker):
    mock_response = {
        "result": {
            "elem": [
                {
                    "text": "Va tutto male anche domani, che credevi?",
                    "short_text": "Bel giorno il giorno dopo",
                    "content_id": "7985824",
                    "content_date": "2018-03-30 00:00:00",
                    "title": "SCORPIONE",
                    "subtitle": "29 Marzo 2018"
                }
            ],
            "datetime": "2018-03-29 00:04:56",
            "timestamp": 1522281896,
            "t_active": "true",
            "t_days": 1,
            "t_frequency_days": 7,
            "ads": "admob",
            "rewarded_video_libs": []
        },
        "id": "5713030"
    }
    mocked_post = mocker.patch('horoscofox.signs.requests.post')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = paolo.scorpio.tomorrow()
    assert resp.text == 'Va tutto male anche domani, che credevi?'
    assert resp.date_start == datetime(2018, 3, 30, 0, 0).date()
    assert resp.date_end == datetime(2018, 3, 31, 0, 0).date()

    resp = paolo.get(sign='scorpio', kind='tomorrow')
    assert resp.text == 'Va tutto male anche domani, che credevi?'
    assert resp.date_start == datetime(2018, 3, 30, 0, 0).date()
    assert resp.date_end == datetime(2018, 3, 31, 0, 0).date()


def test_client_json_response(mocker):
    mock_response = {
        "result": {
            "elem": [
                {
                    "text": "La brutta persona che eravate un tempo non esiste già più. Ora siete una brutta persona completamente nuova.",
                    "short_text": "La brutta persona che eravate un tempo non esiste già più",
                    "content_id": "12345678",
                    "content_date": "2018-03-26 00:00:00",
                    "title": "VERGINE",
                    "subtitle": "26 Marzo 2018"
                }
            ],
            "datetime": "2018-03-26 00:10:30",
            "timestamp": 1522281896,
            "t_active": "true",
            "t_days": 1,
            "t_frequency_days": 7,
            "ads": "admob",
            "rewarded_video_libs": []
        },
        "id": "12345678"
    }
    mocked_post = mocker.patch('horoscofox.signs.requests.post')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = paolo.get(sign='virgo', kind='week').json()
    assert resp['text'] == 'La brutta persona che eravate un tempo non esiste già più. Ora siete una brutta persona completamente nuova.'
    assert resp['date_start'] == '2018-03-26'
    assert resp['date_end'] == '2018-04-02'
