import ndjson
from data.call_record import CallRecord
from typing import List


def export_to_ndjson(records: List[CallRecord], filepath: str) -> None:
    ndjson_records = ndjson.dumps([r.dict() for r in records])
    with open(filepath, "w") as export_file:
        export_file.write(ndjson_records)
