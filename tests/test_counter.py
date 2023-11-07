import pytest

from aakmer.counter import get_kmer_dict


class TestGetKmerDict:
    @pytest.fixture(scope="class")
    def test_aa_sequence_1(self) -> str:
        return "SYHQFS"

    def test_3mers_dict(self, test_aa_sequence_1: str) -> None:
        assert get_kmer_dict(test_aa_sequence_1, 3) == {
            "SYH": 1,
            "YHQ": 1,
            "HQF": 1,
            "QFS": 1,
        }
