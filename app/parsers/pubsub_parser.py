import base64
import json


class PubSubParser:

    @staticmethod
    def parse(request_json):

        message = request_json["message"]

        payload = base64.b64decode(
            message["data"]
        ).decode()

        return json.loads(payload)