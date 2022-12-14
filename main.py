import json
import sys
from typing import Dict

from src.PriceBasket import PriceBasket

FILE = 'products.json'


def load_products_prices(file: str) -> Dict[str, float]:
    with open(file, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    prices = load_products_prices(FILE)
    basket = PriceBasket(prices)
    basket.load_products(sys.argv[1:])
    basket.print_bill()
