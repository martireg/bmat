import csv
from typing import Union, IO, List


def process_csv(file: Union[IO, str, List[str]]):
    if isinstance(file, str):
        file = file.splitlines()
    return csv.DictReader(file, delimiter=",", quotechar="|")
