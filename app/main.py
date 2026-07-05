from fastapi import FastAPI
from fastapi import Request

from app.services.pubsub_service import PubSubService
from app.services.dependency_service import DependencyService

app = FastAPI()

pubsub = PubSubService()

dependency = DependencyService()


@app.post("/")
async def receive(request: Request):

    body = await request.json()

    incident = pubsub.parse(body)

    impacted = dependency.get_impacted(

        incident.dag_id

    )

    return {

        "failedPipeline": incident.dag_id,

        "severity": incident.severity,

        "impactedPipelines": impacted

    }