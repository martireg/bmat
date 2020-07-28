import csv
from typing import Union, IO, List


def process_csv(file: Union[IO, str, List[str], bytes]):
    if isinstance(file, bytes):
        file = file.decode()
    if isinstance(file, str):
        file = file.splitlines()
    return csv.DictReader(file, delimiter=",", quotechar="|")


def create_csv(data):
    pass  #  TODO