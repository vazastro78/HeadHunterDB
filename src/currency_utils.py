from currency_converter import CurrencyConverter
import os


filename = os.path.join("..", "data", "eurofxref.csv")
my_currency_converter = CurrencyConverter(filename)

if __name__ == "__main__":
    print( my_currency_converter.convert(500, 'USD', 'RUB') )