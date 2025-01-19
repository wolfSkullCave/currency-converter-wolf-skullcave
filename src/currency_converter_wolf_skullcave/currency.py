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

# get currency conversion USD to ZAR
url_dollar = "https://currencyfreaks.com/convert/USD/ZAR/1.0" 
url_euro = "https://currencyfreaks.com/convert/EUR/ZAR/1.0"


def round_up(num):
    return round(
        math.ceil(num * 100) / 100, 2
    )

def get_conversion_rate(url=url_dollar):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    currrency_html = soup.find("div", class_='result')
    currency_text = currrency_html.text
    conversion_rate = float(currency_text.split('=')[1].split('ZAR')[0].strip())

    return conversion_rate



@app.command(help="Takes 1 arugument (currency) and displays the exchange rate.")
def rate(currency: str = typer.Option("USD", "--currency", "-c", help="Specify a currency code.")):
      if currency == 'USD' or currency == '$' or currency == 'usd':
        print(f"$1 = R {round_up(get_conversion_rate(url_dollar))}")
      elif currency == 'EUR' or currency == '€' or currency == 'eur':
        print(f"€1 = R {round_up(get_conversion_rate(url_euro))}")
      else:
        print("Please specify a currency")


@app.command(help="Takes 1-2 aruguments (amount, currency) and displays the exchange rate.")
def convert(num_to_convert: float,
            currency: str = typer.Option("USD", "--currency", "-c", help="Specify a currency code.")):
    if currency == 'USD' or currency == '$' or currency == 'usd':
        print(f"${round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_dollar))}")
    elif currency == 'EUR' or currency == '€' or currency == 'eur':
        print(f"€{round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_euro))}")
    else:
        print("Please specify a currency")


if __name__ == "__main__":
    app()
