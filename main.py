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
    try:
        basket.load_products(sys.argv[1:])
    except ValueError as e:
        print(f'Wrong value for product: {e}')
        print('Available products:', ','.join(prices.keys()))
    else:
        basket.print_bill()
