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
    mocked_post = mocker.patch('horoscofox.sign.requests.post')
    mocked_post.return_value.status_code = 200
    mocked_post.return_value.json.return_value = mock_response

    resp = paolo.scorpio.today()
    assert resp.text == 'Va tutto male'
    assert resp.date_start == datetime(2018, 3, 29, 0, 0)
    assert resp.date_end == datetime(2018, 3, 30, 0, 0)

    resp = paolo.get(sign='scorpio', kind='today')
    assert resp.text == 'Va tutto male'
    assert resp.date_start == datetime(2018, 3, 29, 0, 0)
    assert resp.date_end == datetime(2018, 3, 30, 0, 0)