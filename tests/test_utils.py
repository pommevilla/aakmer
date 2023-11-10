import os
from typing import List, cast

import pytest

from aakmer.FastaSequence import FastaSequence
from aakmer.utils import read_fasta, read_sequences_from_file

TEST_DATA_DIRECTORY = "tests/test_data/sequences"


class TestReaderUtils:
    @pytest.fixture(scope="class")
    def single_test_sequence(self) -> List[FastaSequence]:
        input_file = os.path.join(TEST_DATA_DIRECTORY, "single_nucl.fa")
        fasta_sequences = []
        with open(input_file) as fin:
            for fasta_sequence in read_fasta(fin):
                fasta_sequences.append(fasta_sequence)
        return fasta_sequences

    @pytest.fixture(scope="class")
    def multiple_test_sequences(self) -> List[FastaSequence]:
        input_file = os.path.join(TEST_DATA_DIRECTORY, "multiple_aa.fasta")
        fasta_sequences = []
        with open(input_file) as fin:
            for fasta_sequence in read_fasta(fin):
                fasta_sequences.append(fasta_sequence)
        return fasta_sequences

    def test_correct_number_of_entries(
        self, multiple_test_sequences: List[FastaSequence]
    ) -> None:
        assert len(multiple_test_sequences) == 20

    @pytest.mark.dependency(name="test_read_single_fasta")
    def test_read_single_fasta(self, single_test_sequence: FastaSequence) -> None:
        assert len(single_test_sequence) == 1

    # MyPy doesn't currently infer the type of single_test_sequence, causing the pre-commit hook
    # to fail. For now, explicitly casting it to FastaSequence works, but look into this later.
    @pytest.mark.dependency(depends=["test_read_single_fasta"])
    def test_correct_single_header(self, single_test_sequence: FastaSequence) -> None:
        expected_single_header = "single_test_nucl_sequence"
        actual_single_header = cast(FastaSequence, single_test_sequence[0]).header

        assert expected_single_header == actual_single_header

    def test_read_fasta_files(self) -> None:
        expected_fasta_sequences = [
            FastaSequence(
                header="single_test_nucl_sequence",
                sequence="AAAACCCACCCAAAAAATATTCTTTTGCATCCACTGTCAACTTTTCACAGAAACCCATTAAGTCAGGATCCTTAAGAGTTTCCGAGTGTTCATCTGCTGATATTCCAACAACAAACTCTACCGAGTGTCTGAATTTGCTGCTTGAAAAGAGAGGAGCTTCATCGAGTCAAAACTGTTGGAGAAAGATTTCTCTTGAAGATCTTTTCTGTTCCACTTCAAACCTTCCTTCCCCTACTAAAGGGAATCTCCCAATTATTGCCGACGCTGGTGACCATGGGATTTTATCTTTCAAAGTTTCTGACCTGAAAGAAGATATACCCTCGCAAATATCGACGGCTAAGGAAGAGTCCTTCAGTGGTAATGAAGAAGAAGAAGAAGAAGAAGGTGATGACGATGATAAGATAACCCTTCAGGATTTTGTTTGTAATGAAAAGAACCAAAAAGAAATGGGTGAACAAAGAAATGACGTAAGCTCGTCTTCTTGGGTACAAACTGAGCTGTTGTTTCTTCTCCTAAAGGGAAGTATCGGGAGTAATGATACTCAAACAACACTGAGAAAACCAACCCTGTTTCTGATTCCACATTA",
            )
        ]

        single_test_file = os.path.join(TEST_DATA_DIRECTORY, "single_nucl.fa")

        actual_fasta_sequences = read_sequences_from_file(single_test_file)

        assert len(actual_fasta_sequences) == len(expected_fasta_sequences)
        assert actual_fasta_sequences[0].header == expected_fasta_sequences[0].header

        assert len(actual_fasta_sequences[0]) == len(expected_fasta_sequences[0])
        assert (
            actual_fasta_sequences[0].sequence == expected_fasta_sequences[0].sequence
        )
