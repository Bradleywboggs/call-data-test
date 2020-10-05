from pydantic import BaseModel


class CallRecord(BaseModel):
    id: str
    call_id: str
    agent_name: str
    start_time: str
    end_time: str
    duration: float
    metadata = {}
