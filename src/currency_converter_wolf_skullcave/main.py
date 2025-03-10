""" Converts USD and EUR to ZAR """
"""
v2.0.0 Todo list:
- caluculator method
convert 6 * 10
"""

import decimal
import sys
import typer
from typing_extensions import Annotated
from typing import Optional

from __about__ import __version__
from currency import convert

app = typer.Typer()

# main command
@app.command()
def main(
    currency: str = typer.Option("USD", "-e", "--currency", help="Choose a currency to convert from [usd, eur]."),
    amount: str = typer.Argument('1'),
    version: bool = typer.Option(False, "-v", "--version")
    ):
    if version:
        print(f"v{__version__}")        
    else:
        amount = decimal.Decimal(amount)
        convert(amount, currency)

# entry point
if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        print(f"An error occurred: {e}")
