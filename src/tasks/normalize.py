from typing import Dict, List, Union
import dateutil.parser


_LIST_OF_KNOWN_PROPS = {"ID", "CALL_ID", "START", "END", "CUSTOMER_NAME", "AGENT_NAME"}


def normalize(records: List[Dict[str, Union[str, Dict]]]) -> List[Dict]:
    return [_transform_record(record) for record in records]


def _transform_record(record: Dict[str, str]) -> Dict[str, Union[str, Dict]]:
    return {
        "id": record.get("ID"),
        "call_id": record.get("CALL_ID"),
        "start_time": record.get("START"),
        "end_time": record.get("END"),
        "customer_name": record.get("CUSTOMER_NAME"),
        "agent_name": record.get("AGENT_NAME"),
        "duration": _to_timestamp(record.get("END"))
        - _to_timestamp(record.get("START")),
        "metadata": {
            k.lower(): v for k, v in record.items() if k not in _LIST_OF_KNOWN_PROPS
        },
    }


def _to_timestamp(date_string: str) -> float:
    return dateutil.parser.parse(date_string).timestamp()
