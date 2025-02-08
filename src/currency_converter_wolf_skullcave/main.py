""" Converts USD and EUR to ZAR """
"""
v2.0.0 Todo list:
- caluculator method
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
# import math
import decimal

import typer
from typing_extensions import Annotated
from typing import Optional

from __about__ import __version__

app = typer.Typer()

# get currency conversion USD to ZAR
url_dollar = "https://currencyfreaks.com/convert/USD/ZAR/1.0" 
url_euro = "https://currencyfreaks.com/convert/EUR/ZAR/1.0"

def round_up(num):
    num = decimal.Decimal(num)
    return num.quantize(decimal.Decimal('0.01'))


def get_conversion_rate(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    currrency_html = soup.find("div", class_="result")
    currency_text = currrency_html.text
    conversion_rate = currency_text.split("=")[1].split("ZAR")[0].strip()
    conversion_rate = decimal.Decimal(conversion_rate)

    return conversion_rate

def convert(num_to_convert, currency: str):
    if currency == "USD" or currency == "usd":
        print(f"${round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_dollar))}")
    elif currency == "EUR" or currency == "eur":
        print(f"€{round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_euro))}")
    else:
        print("Please specify a currency")


@app.command()
def main(
    currency: str = typer.Option("USD", "-c", help="Choose an currency to convert from [usd, eur]."),
    amount: str = typer.Argument('1'),
    version: bool = typer.Option(False, "-v", "--version")
    ):
    if version:
        print(f"v{__version__}")
    else:
        amount = decimal.Decimal(amount)
        convert(amount, currency)


if __name__ == "__main__":
    app()
