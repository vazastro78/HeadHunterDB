from currency_converter import CurrencyConverter
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


filename = os.path.join(BASE_DIR, "data", "eurofxref.csv")
my_currency_converter = CurrencyConverter(filename)

if __name__ == "__main__":
    print(my_currency_converter.convert(500, 'USD', 'RUB'))
