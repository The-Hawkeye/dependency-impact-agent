from app.services.metadata_service import MetadataService


class DependencyService:

    def __init__(self):

        self.metadata = MetadataService()

    def get_impacted(self, dag):

        impacted = []

        self.__dfs(

            dag,

            impacted

        )

        return impacted

    def __dfs(self, dag, impacted):

        children = self.metadata.get_children(dag)

        for child in children:

            impacted.append(child)

            self.__dfs(

                child,

                impacted

            )