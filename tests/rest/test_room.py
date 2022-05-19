import json
from unittest import mock
from rentomatic.domain.room import Room

room_dict = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "size": 215,
    "price": 39,
    "longitude": -0.09998975,
    "latitude": 51.75436293,
}

rooms = [Room.from_dict(room_dict)]

@mock.patch("application.rest.room.room_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = rooms
    http_reponse = client.get("/rooms")
    assert json.loads(http_reponse.data.decode("UTF-8")) == [room_dict]
    mock_use_case.assert_called()
    assert http_reponse.status_code == 200
    assert http_reponse.mimetype == "application/json"