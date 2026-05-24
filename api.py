"""
-----------------------------------------------------------------------
 imports
-----------------------------------------------------------------------
"""

import requests
import json

"""
-----------------------------------------------------------------------
 Methods
-----------------------------------------------------------------------
"""


"""
-----------------------------------------------------------------------
    Method Name    : currency_converter()
    arguments      : convert_from      -->     currency to exchange
                     amount            -->     amount to exchange
                     convert_to        -->     exchanging currency
    output         : converted Amount
    description    : This function takes currency type as input and 
                     returns the currency converted by latest exchange
                     rate.
-----------------------------------------------------------------------
"""

def currency_converter(convert_from, amount, convert_to):

    # paramter for get request
    params = {
        "base" : f"{convert_from}",                     # base currency
        "amount" : amount
    }

    # Api endpoint
    url = "https://api.frankfurter.dev/v1/latest"

    print(f"Calculating current exchange rates...")
    r = requests.get(url, params = params)

    data = r.json()

    # pretty data used for testing.
    #pretty_data = json.dumps(data, indent = 4)
    #print(pretty_data)

    target_amount = (data["rates"])[convert_to]

    print(f"{amount} {convert_from} : {target_amount} {convert_to}")


"""
-----------------------------------------------------------------------
    Method Name    : view_history()
    arguments      : None
    output         : list of searches
    description    : This function function returns the whole hostory
                     of user searches on currency exchange.
-----------------------------------------------------------------------
"""

def view_history():
    print("Feature available soon.")


"""
-----------------------------------------------------------------------
    Method Name    : favorites()
    arguments      : None
    output         : list most frequent currency conversion
    description    : This function returns the list of most used 
                     currency convertion method.
-----------------------------------------------------------------------
"""

def favorites():
    print("Feature available soon.")


"""
-----------------------------------------------------------------------
    Method Name    : convert_all()
    arguments      : convert_from       --> currency to convert in every
                                            other currency
    output         : conversion of 'conversion_from' to every possible
                     currency
    description    : This function returns the list of conversion value
                     of the selected currency to every possible currency
                     in world.
-----------------------------------------------------------------------
"""

def convert_all(convert_from):
    print("Feature available soon.")

"""
-----------------------------------------------------------------------
 END
-----------------------------------------------------------------------
"""
