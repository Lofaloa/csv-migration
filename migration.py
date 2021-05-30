#!/usr/bin/python3

import csv
from sodexo import make_sodexo_transaction
from argparse import ArgumentParser

fieldnames = ["date", "source", "destination", "amount", "category"]

def write_transaction(source, target):
    with open(source, "r") as input, open(target, "w+") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        reader = csv.reader(input, delimiter=';')
        writer.writeheader()
        next(reader)
        for row in reader:
            transaction = make_sodexo_transaction(row)
            writer.writerow(transaction)

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", nargs=1, help="path to the source CSV file.", required=True)
    parser.add_argument("-d", "--destination", nargs=1, help="path to the destination CSV file.", required=True)
    parser.add_argument("-t", "--type", nargs=1, help="source type of the input file.", required=False, default="sodexo", choices=["sodexo", "bank"])
    args = parser.parse_args()

    if args.type[0] == "sodexo":
        write_transaction(args.file[0], args.destination[0])
        print(f"Sodexo file at {args.file[0]} migrated and written to {args.destination[0]}")
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()