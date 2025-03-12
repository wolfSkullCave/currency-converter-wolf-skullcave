"""Converts USD and EUR to ZAR"""

import decimal
import sys
import typer
from typing_extensions import Annotated
from typing import Optional

from currency_converter_wolf_skullcave.__about__ import __version__
from currency_converter_wolf_skullcave.currency import convert

app = typer.Typer()


# main command
@app.command()
def main(
    currency: str = typer.Option(
        "USD", "-c", "--currency", help="Choose a currency to convert from [usd, eur]."
    ),
    amount: str = typer.Argument("1"),
    version: bool = typer.Option(
        False, "-v", "--version", help="Show the application's version and exit."
    ),
):
    if version:
        print(f"v{__version__}")
        raise typer.Exit()
    else:
        amount = decimal.Decimal(amount)
        convert(amount, currency)


# entry point
if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        print(f"An error occurred: {e}")
