import os

from click.testing import CliRunner

from aakmer.cli import read_fasta, test

TEST_DATA_DIRECTORY = "tests/test_data/sequences"


class TestCLI:
    def test_hello_world(self) -> None:
        runner = CliRunner()
        result = runner.invoke(test, ["World"])

        assert result.exit_code == 0
        assert result.output == "Hello, World!\n"

    def test_read_fasta(self, tmp_path: str) -> None:
        runner = CliRunner()

        input_file = os.path.join(TEST_DATA_DIRECTORY, "single_nucl.fa")
        output_file = os.path.join(tmp_path, "test.out")

        result = runner.invoke(
            read_fasta,
            ["-i", input_file, "-o", output_file],
        )

        assert os.path.isfile(output_file)
        assert result.exit_code == 0

        num_lines = sum(1 for _ in open(output_file))

        assert num_lines == 3
