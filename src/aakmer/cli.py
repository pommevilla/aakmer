import os

import click

from aakmer.utils import read_sequences_from_file

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("name", type=str, default="World")
@click.option("-v", "--verbose", count=True, help="Verbosity level")
@click.option(
    "--times", "-t", type=int, default=1, show_default=True, help="number of greetings"
)
def test(name: str, times: int, verbose: int) -> None:
    """Say hi to NAME, optionally repeating this TIMES times."""
    if verbose:
        click.echo(f"Verbosity level: {verbose}")

    name = name.title()
    for _ in range(times):
        click.echo(f"Hello, {name}!")


@click.command()
@click.option("-i", "--input", type=str, help="fasta file", required=True)
@click.option("-o", "--output", type=str, help="output file", required=True)
def read_fasta(file_input: str, output: str) -> None:
    if not os.path.isfile(file_input):
        raise FileNotFoundError(f"File {file_input} not found")

    if not os.path.dirname(output):
        os.makedirs(os.path.dirname(output), exist_ok=True)

    sequences = read_sequences_from_file(file_input)
    click.echo(f"Found {len(sequences)} sequences in {file_input}")
    click.echo(f"Writing out to {output}...")

    with open(output, "w") as fout:
        fout.write(f"Input file: {file_input}\n")
        fout.write(f"Output file: {output}\n")
        fout.write(f"Found {len(sequences)} sequences\n")
