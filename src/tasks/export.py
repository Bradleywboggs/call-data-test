import ndjson
from typing import Dict, List, Union


def export_to_ndjson(records: List[Dict[str, Union[str, Dict]]], filepath: str) -> None:
    ndjson_records = ndjson.dumps(records)
    with open(filepath, "w") as export_file:
        export_file.write(ndjson_records)
