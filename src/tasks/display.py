from data.call_summary import CallSummary


def print_summary(summary: CallSummary) -> None:
    print(f"Total duration: {summary.total_duration}")
    print("Agent durations:")
    for agent, duration in summary.agent_durations.items():
        print(f"\t{agent.title()}: {duration}")
