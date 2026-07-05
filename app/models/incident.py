from pydantic import BaseModel


class Incident(BaseModel):

    dag_id: str

    severity: str | None = None

    message: str | None = None