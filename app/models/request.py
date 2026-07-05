from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    dag_id: str