import uuid
from rentomatic.domain import Room

def test_room_model_init():
    code = uuid.uuid4()
    room = Room(
        code, 
        size = 200,
        price = 10,
        longitude = -0.09998975,
        latitude = 51.323423
    )
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.323423

def test_room_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.323423   
    }
    room = Room.from_dict(init_dict)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.323423