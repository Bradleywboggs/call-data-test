from pydantic import BaseModel
from typing import Dict


class CallSummary(BaseModel):
    total_duration: int
    agent_durations: Dict[str, int]
