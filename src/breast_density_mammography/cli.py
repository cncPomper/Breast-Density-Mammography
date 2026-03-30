"""Console script for breast_density_mammography."""

import typer
from rich.console import Console

from breast_density_mammography import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for breast_density_mammography."""
    console.print("Replace this message by putting your code into breast_density_mammography.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
