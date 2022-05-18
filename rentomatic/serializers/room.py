import json

class RoomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = o.to_dict()
            to_serialize['code'] = str(to_serialize['code'])
            return to_serialize
        except AttributeError:
            return super().default(o)