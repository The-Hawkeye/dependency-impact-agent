from google.cloud import logging


class LoggingService:

    def __init__(self):

        self.client = logging.Client()

    def fetch_failure_logs(self, dag):

        filter_string = f"""
resource.type="cloud_composer_environment"

severity>=ERROR

textPayload:"{dag}"
"""

        entries = self.client.list_entries(

            filter_=filter_string,

            page_size=20

        )

        logs = []

        for entry in entries:

            logs.append({

                "timestamp": str(entry.timestamp),

                "severity": entry.severity,

                "payload": entry.payload

            })

        return logs