#!/usr/bin/python3

import csv
import datetime
from sodexo import make_sodexo_transaction
from parse import parse

COLUMNS = 3
DESCRIPTION_INDEX = 1
AMOUNT_INDEX = 2
path = "/home/logan/Documents/data_sodexo.csv"

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