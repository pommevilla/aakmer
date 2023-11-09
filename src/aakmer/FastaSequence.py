"""
Generic fasta sequence class.
"""
from dataclasses import dataclass
from typing import Iterator, Union


@dataclass(frozen=True)
class FastaSequence:
    header: str
    sequence: str

    def __len__(self) -> int:
        return len(self.sequence)

    def __iter__(self) -> Iterator[str]:
        yield from self.sequence

    def __str__(self) -> str:
        return f">{self.header}\n{self.sequence}"

    def __repr__(self) -> str:
        header = self.header if len(self.header) <= 5 else f"{self.header[:5]}..."
        sequence = (
            self.sequence if len(self.sequence) <= 5 else f"{self.sequence[:5]}..."
        )
        return f"FastaSeq(header={header}, seq={sequence})"

    def __contains__(self, x: str) -> bool:
        return x in self.sequence

    def __getitem__(self, i: Union[int, slice]) -> str:
        return self.sequence[i]
