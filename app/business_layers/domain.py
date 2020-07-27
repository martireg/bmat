from dataclasses import dataclass
from typing import List


@dataclass
class Work:
    title: str
    contributors: List[str]
    iswc: str
    source: str
    id: int

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: v for k, v in data.items() if not k.startswith("_")})

    def __eq__(self, other):
        return self.__dict__ == other
