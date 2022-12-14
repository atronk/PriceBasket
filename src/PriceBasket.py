from collections import defaultdict
from decimal import Decimal
from typing import Dict, List


class PriceBasket:
    def __init__(self, prices: Dict) -> None:
        for k, v in prices.items():
            # using Decimal to store exact price values
            prices[k] = Decimal(str(v))
        self.prices = prices
        self.products = defaultdict(int)

    def load_products(self, products: List) -> None:
        for prod in products:
            if prod not in self.prices:
                raise ValueError(prod)
            self.products[prod] += 1

    def __get_subtotal(self) -> Decimal:
        subtotal = Decimal(0)
        for product in self.products.keys():
            subtotal += self.prices[product] * self.products[product]
        return subtotal

    def __offer_apples(self) -> Dict[str, Decimal]:
        discount = self.products['Apples'] * self.prices['Apples'] * Decimal('0.1')
        return {'Apples 10% off': discount}

    def __offer_two_soup_tins(self) -> Dict[str, Decimal]:
        loafs = self.products['Bread']
        discountable = self.products['Soup'] // 2
        discounted = 0
        # counts how many loafs of bread can be discount for each pair of soup tins
        while discountable > 0 and loafs > 0:
            discounted += 1
            discountable -= 1
            loafs -= 1
        return {'50% bread discount': discounted * self.prices['Bread'] * Decimal('0.5')}

    def __count_offers(self) -> Dict[str, Decimal]:
        result = dict()
        result.update(self.__offer_apples())
        result.update(self.__offer_two_soup_tins())
        return {k: v for k, v in result.items() if v != 0}

    @staticmethod
    def __format_price(price: Decimal) -> str:
        if price < 1:
            return f'{str(int(price * 100))}p'
        return f'£{price:.2f}'

    def print_bill(self) -> None:
        sub = self.__get_subtotal()
        offers = self.__count_offers()
        total = sub - sum(v for v in offers.values())
        if len(offers) == 0:
            print(f'Subtotal: {self.__format_price(sub)} (No offers available)')
        else:
            print(f'Subtotal: {self.__format_price(sub)}')
            for k, v in offers.items():
                print(f'{k}: {self.__format_price(v)}')
        print(f'Total price: {self.__format_price(total)}')
