import pytest
import uuid
from unittest import mock
from rentomatic.domain.room import Room
from rentomatic.requests.room_list import RoomListRequest
from rentomatic.use_cases.room_list import room_list_use_case

@pytest.fixture
def domain_rooms():
    room1 = Room(
        code = uuid.uuid4(),
        size = 200,
        price = 55,
        longitude = -0.09998975,
        latitude = 51.323423   
    )
    room2 = Room(
        code = uuid.uuid4(),
        size = 215,
        price = 39,
        longitude = -0.18798975,
        latitude = 51.993423   
    )
    room3 = Room(
        code = uuid.uuid4(),
        size = 115,
        price = 70,
        longitude = 0.27998975,
        latitude = 51.443423   
    )
    room4 = Room(
        code = uuid.uuid4(),
        size = 93,
        price = 48,
        longitude = 0.33998975,
        latitude = 51.399423   
    )
    return [room1, room2, room3, room4]

def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    request = RoomListRequest()

    response = room_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with()
    assert response.value == domain_rooms