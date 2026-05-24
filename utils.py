"""
-----------------------------------------------------------------------
 Imports
-----------------------------------------------------------------------
"""

import csv
import os
from datetime import datetime

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
                                   date
                                   time
-----------------------------------------------------------------------
"""

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode = "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["srno", "convert_from", "amount", "convert_to", "date", "time"])



"""
-----------------------------------------------------------------------
 
-----------------------------------------------------------------------
"""

def save_to_csv(convert_from, amount, convert_to):
    with open(CSV_FILE, mode = "a", newline = "") as file:
        writer = csv.writer(file)

        srno = sum(1 for _ in open(CSV_FILE))
        now = datetime.now()

        writer.writerow([
            srno,
            convert_from,
            amount,
            convert_to,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

"""
-----------------------------------------------------------------------
 END
-----------------------------------------------------------------------
"""