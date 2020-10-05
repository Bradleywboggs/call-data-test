from functools import reduce
from typing import Dict, List
from data.call_record import CallRecord
from data.call_summary import CallSummary


def summarize(records: List[CallRecord]) -> CallSummary:
    summ = {"total_duration": 0, "agent_durations": {}}
    for r in records:
        summ = {
            "total_duration": int(r.duration) + summ.get("total_duration"),
            "agent_durations": _aggregate_agent_durations(
                summ.get("agent_durations"), r
            ),
        }
    return CallSummary(**summ)

    # return CallSummary(**reduce(
    #     # "summarizing" function
    #     lambda summ, r: {
    #         "total_duration": int(r.duration)
    #         + summ.get("total_duration"),
    #         "agent_durations": _aggregate_agent_durations(
    #             summ.get("agent_durations"), r
    #         ),
    #     },
    #     # list of CallRecords to be "summarized"
    #     records,
    #     # initial value of "summ"ary above
    #     {"total_duration": 0, "agent_durations": {}},
    # ))


def _aggregate_agent_durations(agent_durations: Dict[str, int], record: CallRecord):
    agent_name = record.agent_name
    duration = record.duration
    initial_total = agent_durations.get(agent_name, 0)
    return {**agent_durations, agent_name: int(duration) + int(initial_total)}
