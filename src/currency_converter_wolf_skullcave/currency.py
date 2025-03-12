from bs4 import BeautifulSoup
from urllib.request import urlopen
import decimal
import sys

url_dollar_array = [
    "https://currencyfreaks.com/convert/USD/ZAR/1.0",
    "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ZAR",
]
url_euro_array = [
    "https://currencyfreaks.com/convert/EUR/ZAR/1.0",
    "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=ZAR",
]


def round_up(num):
    num = decimal.Decimal(num)
    return num.quantize(decimal.Decimal("0.01"))


def bs4_open_url(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_conversion_rate(url_array):
    try:
        for url in url_array:
            soup = bs4_open_url(url)
            if soup:
                if "currencyfreaks" in url:
                    currrency_html = soup.find("div", class_="result")
                    currency_text = currrency_html.text
                    conversion_rate = (
                        currency_text.split("=")[1].split("ZAR")[0].strip()
                    )
                elif "xe" in url:
                    currrency_html = soup.find("p", class_="sc-294d8168-1 hVDvqw")
                    currency_text = currrency_html.text
                    conversion_rate = currency_text.split(" ")[0]

                conversion_rate = decimal.Decimal(conversion_rate)
                return conversion_rate

        raise ValueError("No valid URL found in the array.")

    except Exception as e:
        print(f"An error occurred while fetching the conversion rate: {e}")
        sys.exit(1)


def convert(num_to_convert, currency: str):
    if currency == "USD" or currency == "usd":
        print(
            f"${round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_dollar_array))}"
        )
    elif currency == "EUR" or currency == "eur":
        print(
            f"€{round_up(num_to_convert)} = R {round_up(num_to_convert * get_conversion_rate(url_euro_array))}"
        )
    else:
        print("Please specify a currency")
