# PriceBasket
A program that can price a basket of products taking into account some special offers. The program accepts a list of products into a shopping basket and then outputs the subtotal, and the special offer discounts with the final price.
Here I used <b>Decimal</b> type for manipulating prices/cost, <b>defaultdict</b> with integers for counting the products, <b>pytest</b> for unit tests.

To launch the program, follow the steps:
1. Git clone or download the program: https://github.com/atronk/PriceBasket
2. Make sure Python3 is installed on the system.
3. Optionally: set up the virtual environment with <code>python3 -m venv ./env</code> and start it with the script. On windows: <code>.\env\Scripts\activate</code> , on Mac/Linux: <code>source ./env/bin/activate</code> .
4. Install packages with <code>pip install -r requirements.txt</code>
5. Run the tests: <code>python -m pytest .</code>
6. Run the program: <code>python main.py Apples Bread Milk Soup</code>
