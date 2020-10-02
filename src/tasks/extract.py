import csv
from typing import Dict, List, Union

# NOTE depending on the potential size of the data files, using a generator may be
#   a better option here, however for purposes of this exercise and this particular file,
#   we'll simply parse the file.


def get_data(file_name) -> List[Dict[str, Union[str, Dict]]]:
    with open(file_name, newline="") as data_file:
        return list(csv.DictReader(data_file))
