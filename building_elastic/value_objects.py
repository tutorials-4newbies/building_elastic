import dataclasses
from typing import List


@dataclasses.dataclass
class Review:
    identifier: int
    text: str

    def __repr__(self):
        return f"{self.identifier} - {self.text}"


@dataclasses.dataclass
class Response:
    count: int
    samples: List[Review]

    def __repr__(self):
        responses = "\n".join([f"{sample.identifier} - {sample.text}" for sample in self.samples])
        return f"count:{self.count} \n responses:\n {responses}"