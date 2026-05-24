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
from utils import init_csv
from utils import save_to_csv


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
choose : """

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

init_csv()

while True:

    # non integer input validation handled
    try:
        choose_menu = int(input(menu))
    except ValueError:
        print("\nError! : Only Numbers are excepted.Between 1-5")
        print("Direction : Try again.\n")
        continue

    match (choose_menu):
        case 1:
            print("--- Currency Converter ---")
            print(currencies)

            # Validation for convert_from
            while True:
                try:
                    convert_from = int(input("Convert From : "))
                    if convert_from <= 0 or convert_from > 10:
                        print("Error : Please only select between 1 to 10")
                    else:
                        break
                except ValueError:
                    print("Error : Only Numbers are expected.")
                    continue

            currency_from_name = currency_num_to_name[convert_from]
            print(f"( {currency_from_name} )")

            # validation for amount
            while True:
                try:
                    amount = int(input("Amount : "))
                    if amount <= 0:
                        print("Error : Amount must be greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Error : Only Numbers are expected.")
                    continue

            # validation for convert to
            while True:
                try:
                    convert_to = int(input("Convert To : "))
                    if convert_to <= 0 or convert_to > 10:
                        print("Error : Please only select between 1 to 10")
                    elif convert_to == convert_from:
                        print("Cannot select same currency.")
                    else:
                        break
                except ValueError:
                    print("Error : Only Numbers are expected.")
                    continue

            currency_to_name = currency_num_to_name[convert_to]
            print(f"( {currency_to_name} )")

            print(f"\n{amount} {currency_from_name} to {currency_to_name}\n")

            print(f"Calculating current exchange rates...")
            result = currency_converter(currency_from_name, amount, currency_to_name)
            print(f"{amount} {currency_from_name} --> {result} {currency_to_name}")

            save_to_csv(currency_from_name, amount, currency_to_name)

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

        case _:
            print("Invalid Choice, Please select between 1-10.")

"""
-----------------------------------------------------------------------
 END
-----------------------------------------------------------------------
"""