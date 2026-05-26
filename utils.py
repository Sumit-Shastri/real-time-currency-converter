"""
-----------------------------------------------------------------------
 Imports
-----------------------------------------------------------------------
"""

import csv
import os
from datetime import datetime
import pandas

"""
-----------------------------------------------------------------------
 Data
-----------------------------------------------------------------------
"""

CSV_FILE = "history.csv"

"""
-----------------------------------------------------------------------
 Methods
-----------------------------------------------------------------------
"""

"""
----------------------------------------------------------------------- 
    Method Name    : init_csv()
    arguments      : None
    output         : File --> history.csv
    description    : This function checks if CSV_FILE exists, if no
                     it creates with certain column names
                     column_name : srno
                                   convert_from
                                   amount
                                   convert_to
                                   result
                                   date
                                   time
-----------------------------------------------------------------------
"""

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode = "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["srno", "convert_from", "amount", "convert_to", "result", "date", "time"])



"""
-----------------------------------------------------------------------
    Method Name    : save_to_csv()
    arguments      : convert_from      -->     currency to exchange
                     amount            -->     amount to exchange
                     convert_to        -->     exchanging currency
                     result            -->     calculated result
    output         : writes data to csv file.
    description    : This function appends the given data to csv file.
                      data :       srno
                                   convert_from
                                   amount
                                   convert_to
                                   result
                                   date
                                   time
-----------------------------------------------------------------------
"""

def save_to_csv(convert_from, amount, convert_to, result):
    with open(CSV_FILE, mode = "a", newline = "") as file:
        writer = csv.writer(file)

        srno = sum(1 for _ in open(CSV_FILE))
        now = datetime.now()

        writer.writerow([
            srno,
            convert_from,
            amount,
            convert_to,
            result,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

"""
-----------------------------------------------------------------------
    Method Name    : view_history()
    arguments      : None
    output         : list of searches
    description    : This function function returns the whole history
                     of user searches on currency exchange.
-----------------------------------------------------------------------
"""

def view_history():
    data = pandas.read_csv(CSV_FILE)
    last_10_data = data.tail(10).reset_index(drop=True)  # reset to 0-9
    history_list = []

    for i in range(len(last_10_data)):
        row = last_10_data.iloc[i]
        message = f"{i+1}. {row['amount']} {row['convert_from']} --> {row['result']} {row['convert_to']} ({row['date']} | {row['time']})"
        history_list.append(message)

    return history_list


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
    favorite = pandas.read_csv(CSV_FILE)

    favorite["pair"] = favorite["convert_from"] + " -> " + favorite["convert_to"]
    top3 = favorite["pair"].value_counts().head(3)

    return top3

"""
-----------------------------------------------------------------------
 END
-----------------------------------------------------------------------
"""