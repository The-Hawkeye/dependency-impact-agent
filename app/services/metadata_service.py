import json


class MetadataService:

    def __init__(self):

        with open(
            "app/data/dag_metadata.json"
        ) as f:

            self.metadata = json.load(f)

    def get_children(self, dag):

        return self.metadata.get(

            dag,

            {}

        ).get(

            "children",

            []
        )