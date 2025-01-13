"""
This module contains functions for currency conversion.

The conversion is done by scraping the website: https://currencyfreaks.com/

The conversion rate is rounded up to the nearest cent.

The functions are:
- round_up(num): rounds up the given number to the nearest cent.
- main(): scrapes the website and prints out the conversion of $1 and a
specified amount to Rand.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import typer

app = typer.Typer()


def round_up(num):
    return round(
        math.ceil(num * 100) / 100, 2
    )

# get currency conversion USD to ZAR
url = "https://currencyfreaks.com/convert/USD/ZAR/1.0"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

currrency_html = soup.find("div", class_='result')
currency_text = currrency_html.text
conversion_rate = float(currency_text.split('=')[1].split('ZAR')[0].strip())


@app.command()
def rate():
      print(f"$1 = R {round_up(conversion_rate)}")

@app.command()
def convert(num_to_convert: float):
        print (f"${round_up(num_to_convert)} = R {round_up(num_to_convert * conversion_rate)}")


if __name__ == "__main__":
    app()