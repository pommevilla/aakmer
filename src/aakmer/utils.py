"""
This module contains various utilities used during in silico PCR.
"""

from typing import Iterator, List, TextIO

from aakmer.FastaSequence import FastaSequence


def read_fasta(fasta_file: TextIO) -> Iterator[FastaSequence]:
    """An iterator for fasta files.

    Inputs
    ------
    fasta_file: TextIO
        An open file for reading

    Outputs
    -------
    An iterator yielding the the sequence names and sequences from a fasta file

    Example
    -------
    input_file = 'tests/test_data/sequences/met_r.fa.fasta'
    with open(input_file) as fin:
        for name, seq in read_fasta(fin):
            print(f'{name}\n{seq}')

    """
    name = None
    seq: List[str] = []
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                header = name
                sequence = "".join(seq)
                yield FastaSequence(header, sequence)
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name:
        header = name
        sequence = "".join(seq)
        yield FastaSequence(header, sequence)


def read_sequences_from_file(primer_file: str) -> List[FastaSequence]:
    """
    Reads a fasta file, converts the sequences to FastaSequences, and returns them in a list.

    Inputs:
    -------
    primer
    """
    sequences = []
    with open(primer_file) as fin:
        for fasta_sequence in read_fasta(fin):
            sequences.append(fasta_sequence)

    return sequences


class InvalidColumnSelectionError(Exception):
    pass
