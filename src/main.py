import os
from tasks.retriever import get_data
from tasks.normalizer import normalize
from tasks.summarizer import summarize
from tasks.printer import print_summary
from tasks.exporter import export_to_ndjson

DATA_SOURCE = os.environ.get("DATA_SOURCE") or "../sample_call_data.csv"
DESTINATION = os.environ.get("DESTINATION") or "../exported-sample_call_data.ndjson"


def main():
    parsed_data = get_data(DATA_SOURCE)
    normalized_data = normalize(parsed_data)
    summary = summarize(normalized_data)

    export_to_ndjson(normalized_data, DESTINATION)
    print_summary(summary)


if __name__ == "__main__":
    main()
