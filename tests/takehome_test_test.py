import os.path
from src import normalizer, exporter, retriever, summarizer

_FILE_PATH = "./tests/test-sample-data.csv"

records_from_csv = [
    {
        "ACW": "7",
        "ADDR": "20.128.243.133",
        "AGENT_NAME": "Scott Lopez",
        "CALL_ID": "971-605-3989x98841",
        "CUSTOMER_NAME": "Lisa Rosales",
        "END": "08/02/2020 9:23:25 AM",
        "ID": "84ef8-bfede-7972af",
        "START": "08/02/2020 9:12:26 AM",
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like Gecko) Version/4.0.1 Safari/531.8.1",
    },
    {
        "ACW": "7",
        "ADDR": "105.0.200.198",
        "AGENT_NAME": "Paul Duncan",
        "CALL_ID": "001-634-775-4898x281",
        "CUSTOMER_NAME": "Sean Allen",
        "END": "08/05/2020 5:59:30 PM",
        "ID": "aad94-4669d-e72ece",
        "START": "08/05/2020 5:49:10 PM",
        "USER_AGENT": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS X) AppleWebKit/534.2 (KHTML, like Gecko) CriOS/27.0.855.0 Mobile/58M631 Safari/534.2",
    },
    {
        "ACW": "7",
        "ADDR": "186.245.251.226",
        "AGENT_NAME": "Mr. Kyle Miller",
        "CALL_ID": "457.228.0765x8971",
        "CUSTOMER_NAME": "Christopher Garcia",
        "END": "08/05/2020 7:06:08 PM",
        "ID": "3d04b-35911-1052d3",
        "START": "08/05/2020 6:52:06 PM",
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2020-09-07 19:03:14 Firefox/3.8",
    },
]

transformed = [
    {
        "agent_name": "Scott Lopez",
        "call_id": "971-605-3989x98841",
        "customer_name": "Lisa Rosales",
        "duration": 659.0,
        "end_time": "08/02/2020 9:23:25 AM",
        "id": "84ef8-bfede-7972af",
        "metadata": {
            "acw": "7",
            "addr": "20.128.243.133",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 "
            "rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like "
            "Gecko) Version/4.0.1 Safari/531.8.1",
        },
        "start_time": "08/02/2020 9:12:26 AM",
    },
    {
        "agent_name": "Paul Duncan",
        "call_id": "001-634-775-4898x281",
        "customer_name": "Sean Allen",
        "duration": 620.0,
        "end_time": "08/05/2020 5:59:30 PM",
        "id": "aad94-4669d-e72ece",
        "metadata": {
            "acw": "7",
            "addr": "105.0.200.198",
            "user_agent": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS "
            "X) AppleWebKit/534.2 (KHTML, like Gecko) "
            "CriOS/27.0.855.0 Mobile/58M631 Safari/534.2",
        },
        "start_time": "08/05/2020 5:49:10 PM",
    },
    {
        "agent_name": "Mr. Kyle Miller",
        "call_id": "457.228.0765x8971",
        "customer_name": "Christopher Garcia",
        "duration": 842.0,
        "end_time": "08/05/2020 7:06:08 PM",
        "id": "3d04b-35911-1052d3",
        "metadata": {
            "acw": "7",
            "addr": "186.245.251.226",
            "user_agent": "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2020-09-07 19:03:14 Firefox/3.8",
        },
        "start_time": "08/05/2020 6:52:06 PM",
    },
]


def test_raw_data_loader_generates_dictionary_from_csv():
    actual = retriever.get_data(_FILE_PATH)
    expected = [
        {
            "ACW": "7",
            "ADDR": "20.128.243.133",
            "AGENT_NAME": "Scott Lopez",
            "CALL_ID": "971-605-3989x98841",
            "CUSTOMER_NAME": "Lisa Rosales",
            "END": "08/02/2020 9:23:25 AM",
            "ID": "84ef8-bfede-7972af",
            "START": "08/02/2020 9:12:26 AM",
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like Gecko) Version/4.0.1 Safari/531.8.1",
        },
        {
            "ACW": "7",
            "ADDR": "105.0.200.198",
            "AGENT_NAME": "Paul Duncan",
            "CALL_ID": "001-634-775-4898x281",
            "CUSTOMER_NAME": "Sean Allen",
            "END": "08/05/2020 5:59:30 PM",
            "ID": "aad94-4669d-e72ece",
            "START": "08/05/2020 5:49:10 PM",
            "USER_AGENT": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS X) AppleWebKit/534.2 (KHTML, like Gecko) CriOS/27.0.855.0 Mobile/58M631 Safari/534.2",
        },
        {
            "ACW": "7",
            "ADDR": "186.245.251.226",
            "AGENT_NAME": "Mr. Kyle Miller",
            "CALL_ID": "457.228.0765x8971",
            "CUSTOMER_NAME": "Christopher Garcia",
            "END": "08/05/2020 7:06:08 PM",
            "ID": "3d04b-35911-1052d3",
            "START": "08/05/2020 6:52:06 PM",
            "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2020-09-07 19:03:14 Firefox/3.8",
        },
    ]

    assert expected == actual


def test_transform_record_returns_transformed_record():
    actual = normalizer._transform_record(records_from_csv[0])
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


def test_normalize_records_record_returns_all_records_normalized():
    actual = normalizer.normalize(records_from_csv)
    expected = transformed

    assert actual == expected


def test_summarize_creates_summary_dictionary():
    actual = summarizer.summarize(transformed)
    expected = {
        "total_durations": 2121,
        "agent_durations": {
            "Mr. Kyle Miller": 842,
            "Paul Duncan": 620,
            "Scott Lopez": 659,
        },
    }

    assert expected == actual


def test_export_json_to_file_exports_file():
    filepath = "./tests/exported.ndjson"
    # set up: delete the file, if it's already present
    if os.path.isfile(filepath):
        os.remove(filepath)

    exporter.export_to_ndjson(transformed, filepath)
    assert os.path.isfile(filepath)
