import base64
import json

from app.models.incident import Incident


class PubSubService:

    def parse(self, body):

        message = body["message"]

        decoded = base64.b64decode(

            message["data"]

        ).decode()

        payload = json.loads(decoded)

        #
        # Temporary
        #
        # Until we parse Composer logs
        #

        return Incident(

            dag_id="customer_pipeline",

            severity="ERROR",

            message=str(payload)

        )