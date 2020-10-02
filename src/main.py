import os
from tasks.extract import get_data
from tasks.normalize import normalize
from tasks.summarize import summarize
from tasks.display import print_summary
from tasks.export import export_to_ndjson

DATA_SOURCE = os.environ.get("DATA_SOURCE", "../sample_call_data.csv")
DESTINATION = os.environ.get("DESTINATION", "../exported-sample_call_data.ndjson")


def main():
    parsed_data = get_data(DATA_SOURCE)
    normalized_data = normalize(parsed_data)
    summary = summarize(normalized_data)

    export_to_ndjson(normalized_data, DESTINATION)
    print_summary(summary)


if __name__ == "__main__":
    main()
