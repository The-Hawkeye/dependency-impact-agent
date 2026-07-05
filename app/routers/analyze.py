from fastapi import APIRouter

from app.parsers.pubsub_parser import PubSubParser

from app.parsers.composer_log_parser import ComposerLogParser

from app.services.logging_service import LoggingService

from app.services.airflow_service import AirflowService


router = APIRouter()


@router.post("/analyze")
def analyze(body: dict):

    event = PubSubParser.parse(body)

    incident = ComposerLogParser.parse(event)

    logging_service = LoggingService()

    logs = logging_service.fetch_failure_logs(

        incident.dag_id

    )

    airflow = AirflowService(

        "YOUR_COMPOSER_URL"

    )

    dag = airflow.get_dag(

        incident.dag_id

    )

    run = airflow.get_latest_run(

        incident.dag_id

    )

    return {

        "incident": incident,

        "dag": dag,

        "latestRun": run,

        "logs": logs

    }