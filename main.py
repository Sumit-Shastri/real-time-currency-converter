"""
-----------------------------------------------------------------------
 Imports
-----------------------------------------------------------------------
"""

import sys
from api import currency_converter
from api import view_history
from api import favorites
from api import convert_all


"""
-----------------------------------------------------------------------
 Main
-----------------------------------------------------------------------
"""

menu = """
------------------------------------------------------
1. Convert Currency
2. View history
3. Favorites
4. Convert All
5. Exit
------------------------------------------------------\n
"""

currencies = """
------------------------------------------------------
1. INR ( Indian Rupee )
2. USD ( United State Dollar )
3. EUR ( EURO ) 
4. JPY ( Japanese YEN )
5. GBP ( British Pound )
6. CNY ( Chinese Yuan )
7. CHF ( Swiss Franc )
8. AUD ( Australian Dollar )
9. CAD ( Canadian Dollar )
10. NZD ( New Zealand Dollar )
------------------------------------------------------\n
"""

currency_num_to_name = {
    1 : "INR",
    2 : "USD",
    3 : "EUR",
    4 : "JPY",
    5 : "GBP",
    6 : "CNY",
    7 : "CHF",
    8 : "AUD",
    9 : "CAD",
    10 : "NZD"
}

print("\n---   Welcome to Real-Time-Currency-COnverter   ---\n")

while(True):
    choose_menu = int(input(menu))

    match (choose_menu):
        case 1:
            print("--- Currency Converter ---")
            print(currencies)

            convert_from = int(input("Convert From : "))
            currency_from_name = currency_num_to_name[convert_from]
            print(f"( {currency_from_name} )")

            amount = int(input("Amount : "))

            convert_to = int(input("Convert To : "))
            currency_to_name = currency_num_to_name[convert_to]
            print(f"( {currency_to_name} )")


            print(f"\n{amount} {currency_from_name} to {currency_to_name}\n")

            currency_converter(currency_from_name, amount, currency_to_name)

        case 2:
            print("--- View History ---")

            view_history()

        case 3:
            print("--- Favorites ---")

            favorites()

        case 4:
            print("--- Convert All ---")

            convert_from = input("Enter currency code (eg. INR) : ")

            convert_all(convert_from)

        case 5:
            print("Exiting ...")
            sys.exit()

"""
-----------------------------------------------------------------------
 END
-----------------------------------------------------------------------
"""