from typing import Dict


def print_summary(summary: Dict) -> None:
    print(f"Total duration: {summary.get('total_durations')}")
    print("Agent durations:")
    for agent, duration in summary.get("agent_durations").items():
        print(f"\t{agent.title()}: {duration}")
