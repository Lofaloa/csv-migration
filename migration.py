#!/usr/bin/python3

import csv
import datetime
from sodexo import make_sodexo_transaction
from parse import parse

COLUMNS = 3
DESCRIPTION_INDEX = 1
AMOUNT_INDEX = 2
path = "/home/logan/Documents/data_sodexo.csv"

def clean_date(date):
    if type(date) is str:
        d = datetime.datetime.strptime(date, "%d-%m-%Y").date()
        return d.isoformat()
    else:
        raise TypeError("Invalid date type.")

def clean_payment(description):
    if type(description) is str:
        transaction_ref_idx = description.find("(transaction")
        return description[:transaction_ref_idx].replace("dépense", "").strip()
    else:
        raise TypeError("invalid description type.")

def clean_deposit(description):
    if type(description) is str:
        result = parse("{} eLunch Pass d'une valeur de {} de {}", description)
        return result[2]
    else:
        raise TypeError("Invalid description type.")

def clean_amount(amount):
    if type(amount) is str:
        return amount.replace(" ", "").replace("€", "").replace("+", "")
    else:
        raise TypeError("Invalid amount type.")

def transform(row):
    if len(row) == COLUMNS:
        row[AMOUNT_INDEX] = clean_amount(row[AMOUNT_INDEX])
        amount = float(row[AMOUNT_INDEX])
        row[DESCRIPTION_INDEX] = clean_deposit(row[DESCRIPTION_INDEX]) if amount > 0 else clean_payment(row[DESCRIPTION_INDEX])
        row[0] = clean_date(row[0])
    else:
        raise ValueError("Invalid row: " + str(row))
    return row

def main():
    with open(path) as csvfile:
        index = 0
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if index == 0:
                row[1] = "Source"
                row.append("Destination")
                row.append("Category")
            else:
                transaction = make_sodexo_transaction(row)
                print(transaction)
            index += 1

if __name__ == "__main__":
    main()