from functools import reduce
from typing import Dict, List, Union


def summarize(
    records: List[Dict[str, Union[str, Dict]]]
) -> Dict[str, Union[int, Dict]]:
    return reduce(
        # "summarizing" function
        lambda summ, r: {
            "total_durations": int(r.get("duration") or 0)
            + summ.get("total_durations"),
            "agent_durations": _aggregate_agent_durations(
                summ.get("agent_durations"), r
            ),
        },
        # list of things to be "summarized"
        records,
        # initial value of "summ"ary above
        {"total_durations": 0, "agent_durations": {}},
    )


def _aggregate_agent_durations(
    agent_durations: Dict[str, int], record: Dict[str, Union[str, Dict]]
):
    agent_name = record.get("agent_name")
    duration = record.get("duration") or 0
    initial_total = agent_durations.get(agent_name) or 0
    return {**agent_durations, agent_name: int(duration) + int(initial_total)}


def print_summary(summary: Dict) -> None:
    print(f"Total duration: {summary.get('total_durations')}")
    print("Agent durations:")
    for agent, duration in summary.get("agent_durations").items():
        print(f"\t{agent.title()}: {duration}")
