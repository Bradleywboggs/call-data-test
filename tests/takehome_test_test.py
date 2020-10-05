import os.path
from tasks import export, normalize, extract, summarize
from data.call_record import CallRecord
from data.call_summary import CallSummary
from tests.test_helpers import records_from_csv, transformed

_DATA_SOURCE = "./tests/test-sample-data.csv"
_DESTINATION = "./tests/exported.ndjson"


def test_raw_data_loader_generates_dictionary_from_csv():
    actual = extract.get_data(_DATA_SOURCE)
    expected = records_from_csv
    assert expected == actual


def test_transform_record_returns_transformed_record():
    actual = normalize._transform_record(records_from_csv[0])
    expected = {
        "id": "84ef8-bfede-7972af",
        "call_id": "971-605-3989x98841",
        "start_time": "08/02/2020 9:12:26 AM",
        "end_time": "08/02/2020 9:23:25 AM",
        "customer_name": "Lisa Rosales",
        "agent_name": "Scott Lopez",
        "duration": 659.0,
        "metadata": {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like Gecko) Version/4.0.1 Safari/531.8.1",
            "addr": "20.128.243.133",
            "acw": "7",
        },
    }
    assert expected == actual


def test_call_record_constructor_receives_normalized_raw_data():
    actual = CallRecord(**normalize._transform_record(records_from_csv[0]))
    expected = CallRecord(
        id="84ef8-bfede-7972af",
        call_id="971-605-3989x98841",
        start_time="08/02/2020 9:12:26 AM",
        end_time="08/02/2020 9:23:25 AM",
        customer_name="Lisa Rosales",
        agent_name="Scott Lopez",
        duration=659.0,
        metadata={
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like Gecko) Version/4.0.1 Safari/531.8.1",
            "addr": "20.128.243.133",
            "acw": "7",
        },
    )
    assert expected == actual


def test_normalize_records_record_returns_all_records_normalized():
    actual = normalize.normalize(records_from_csv)
    expected = [CallRecord(**t) for t in transformed]

    assert expected == actual


def test_summarize_creates_summary_dictionary():
    actual = summarize.summarize([CallRecord(**t) for t in transformed])
    expected = {
        "total_duration": 2121,
        "agent_durations": {
            "Mr. Kyle Miller": 842,
            "Paul Duncan": 620,
            "Scott Lopez": 659,
        },
    }

    assert expected == actual


def test_summarize_creates_call_summary():
    actual = summarize.summarize([CallRecord(**t) for t in transformed])
    expected = CallSummary(
        total_duration=2121,
        agent_durations={
            "Mr. Kyle Miller": 842,
            "Paul Duncan": 620,
            "Scott Lopez": 659,
        },
    )

    assert expected == actual


def test_export_ndjson_to_file_exports_file():
    # set up: delete the file, if it's already present
    if os.path.isfile(_DESTINATION):
        os.remove(_DESTINATION)

    export.export_to_ndjson([CallRecord(**t) for t in transformed], _DESTINATION)
    assert os.path.isfile(_DESTINATION)
