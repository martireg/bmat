import csv
from typing import Union, IO, List, Dict, Generator, Iterable, ByteString, Optional


def process_csv(file: Union[IO, str, List[str], bytes]):
    if isinstance(file, bytes):
        file = file.decode()
    if isinstance(file, str):
        file = file.splitlines()
    return csv.DictReader(file, delimiter=",", quotechar="|")


def stream_csv_from_dicts(
    data: List[Dict], keys: Iterable, separator: Optional[str] = None
) -> Generator[ByteString, None, None]:
    if not data:
        yield b""
        return
    if separator is None:
        separator = ","

    yield separator.join(keys).encode()
    yield b"\n"
    for i, obj in enumerate(data):
        items = (
            "|".join(item)
            if isinstance(item := obj.get(key, ""), list)
            else str(item if item is not None else "")
            for key in keys
        )
        yield separator.join(items).encode()
        if i < len(data) - 1:
            yield b"\n"
