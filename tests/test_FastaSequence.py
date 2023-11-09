import pytest

from aakmer.FastaSequence import FastaSequence


class TestFastaSequence:
    @pytest.fixture
    def test_sequence_short(self) -> FastaSequence:
        return FastaSequence("test_short", "MKLVI")

    @pytest.fixture
    def test_sequence_long(self) -> FastaSequence:
        return FastaSequence(
            "test_long", "MKLVILGVLVLLVLVLCVPGSTSLRLNLTGVVTDNGLLCINPLNLFYTLVLVSVFIIFLQ"
        )

    def test_len(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        for fasta_seq in [test_sequence_short, test_sequence_long]:
            assert len(fasta_seq) == len(fasta_seq.sequence)

    def test_iter(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        seq_short = FastaSequence("header_short", test_sequence_short.sequence)
        seq_long = FastaSequence("header_long", test_sequence_long.sequence)
        assert list(seq_short) == list(test_sequence_short.sequence)
        assert list(seq_long) == list(test_sequence_long.sequence)

    def test_str(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        assert str(test_sequence_short) == ">test_short\nMKLVI"
        assert (
            str(test_sequence_long)
            == ">test_long\nMKLVILGVLVLLVLVLCVPGSTSLRLNLTGVVTDNGLLCINPLNLFYTLVLVSVFIIFLQ"
        )

    def test_repr(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        expected_repr_short = "FastaSeq(header=test_..., seq=MKLVI)"
        actual_repr_short = repr(test_sequence_short)
        expected_repr_long = "FastaSeq(header=test_..., seq=MKLVI...)"
        actual_repr_long = repr(test_sequence_long)

        assert expected_repr_short == actual_repr_short
        assert expected_repr_long == actual_repr_long

    def test_contains(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        assert "M" in test_sequence_short
        assert "N" not in test_sequence_short
        assert "LV" in test_sequence_short
        assert "VL" not in test_sequence_short
        assert "M" in test_sequence_long
        assert "W" not in test_sequence_long
        assert "VP" in test_sequence_long
        assert "PV" not in test_sequence_long

    def test_getitem(
        self, test_sequence_short: FastaSequence, test_sequence_long: FastaSequence
    ) -> None:
        assert test_sequence_short[0] == "M"
        assert test_sequence_short[1:3] == "KL"
        assert test_sequence_short[-1] == "I"
        assert test_sequence_short[-2:] == "VI"
        assert test_sequence_long[0] == "M"
        assert test_sequence_long[1:3] == "KL"
        assert test_sequence_long[-1] == "Q"
        assert test_sequence_long[-2:] == "LQ"
