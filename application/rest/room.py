from crypt import methods
import json
from flask import Blueprint, Response
from rentomatic.repository.memrepo import MemRepo
from rentomatic.use_cases.room_list import room_list_use_case
from rentomatic.serializers.room import RoomJSONEncoder

blueprint = Blueprint("room",__name__)

rooms = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    }
]

@blueprint.route("/rooms",methods = ["GET"])
def room_list():
    repo = MemRepo(rooms)
    result = room_list_use_case(repo)
    return Response(
        json.dumps(result, cls = RoomJSONEncoder),
        mimetype = "application/json",
        status = 200
    )