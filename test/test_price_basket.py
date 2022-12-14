import pytest
from decimal import Decimal
from src.PriceBasket import PriceBasket


class TestPriceBasket:
    PRODS_1 = ["Apples", "Bread", "Milk", "Soup"]
    PRODS_2 = ["Apples", "Apples", "Apples", "Milk"]
    PRODS_3 = ["Soup", "Soup", "Bread", "Bread"]
    PRODS_4 = ["Soup", "Soup", "Soup", "Soup", "Bread", "Bread"]
    PRODS_5 = ["Soup", "Bread", "Milk", "Milk"]
    PRODS_6 = ["Soup", "Soup", "Bread", "Milk", "Milk", "Apples", "Apples", "Apples"]

    @pytest.mark.parametrize("prods,amount", [
        (PRODS_1, 4), (PRODS_2, 2), (PRODS_3, 2), (PRODS_4, 2), (PRODS_5, 3), (PRODS_6, 4)])
    def test_load_products(self, prods, amount):
        basket = PriceBasket(pytest.prices)
        basket.load_products(products=prods)
        assert len(basket.products.keys()) == amount
        for prod in prods:
            assert prod in basket.products

    @pytest.mark.parametrize("prods,subtotal", [
        (PRODS_1, Decimal('3.75')),
        (PRODS_2, Decimal('4.3')),
        (PRODS_3, Decimal('2.9')),
        (PRODS_4, Decimal('4.2')),
        (PRODS_5, Decimal('4.05')),
        (PRODS_6, Decimal('7.7'))])
    def test__get_subtotal(self, prods, subtotal):
        basket = PriceBasket(pytest.prices)
        basket.load_products(prods)
        assert basket._PriceBasket__get_subtotal() == subtotal

    @pytest.mark.parametrize("prods,apple,bread", [
        (PRODS_1, Decimal('0.1'), None),
        (PRODS_2, Decimal('0.3'), None),
        (PRODS_3, None, Decimal('0.4')),
        (PRODS_4, None, Decimal('0.8')),
        (PRODS_5, None, None),
        (PRODS_6, Decimal('0.3'), Decimal('0.4'))])
    def test__count_offers(self, prods, apple, bread):
        basket = PriceBasket(pytest.prices)
        basket.load_products(prods)
        offers = basket._PriceBasket__count_offers()
        assert offers.get('Apples 10% off', None) == apple
        assert offers.get('50% bread discount', None) == bread

    @pytest.mark.parametrize("prods,total", [
        (PRODS_1, Decimal('3.65')),
        (PRODS_2, Decimal('4')),
        (PRODS_3, Decimal('2.5')),
        (PRODS_4, Decimal('3.4')),
        (PRODS_5, Decimal('4.05')),
        (PRODS_6, Decimal('7'))])
    def test_print_result(self, prods, total, capfd):
        basket = PriceBasket(pytest.prices)
        basket.load_products(prods)
        basket.print_bill()
        out, err = capfd.readouterr()
        assert str(total) in out
