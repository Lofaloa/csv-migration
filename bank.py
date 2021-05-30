import csv
import parse
from util import clean_date, parse_amount

fieldnames = ["date", "source", "destination", "amount", "category"]

fieldnames_mappings = {
    "date": "Date de comptabilisation",
    "amount": "Montant",
    "me": "Compte",
    "partner_account": "Compte contrepartie",
    "partner": "Nom contrepartie contient",
    "transaction": "Transaction"
}

def get_value(row, name):
    return row[fieldnames_mappings[name]]

def parse_maestro_payment(text):
        results = parse.parse("PAIEMENT MAESTRO{} {} BE{}", text)
        return results[1].title()

def get_partner_text(row):
    name = get_value(row, "partner")
    text = get_value(row, "transaction")

    if name != "":
        return name

    if name == "" and text.startswith("PAIEMENT MAESTRO"):
        print("maestroooooooo")
        return parse_maestro_payment(text)

    return text

def make_bank_deposit(row, category):
    return {
        "date": clean_date(get_value(row, "date"), "%d/%m/%Y"),
        "source": get_partner_text(row),
        "destination": get_value(row, "me").title(),
        "amount": parse_amount(get_value(row, "amount"), ","),
        "category": category
    }

def make_bank_payment(row, category):
    return {
        "date": clean_date(get_value(row, "date"), "%d/%m/%Y"),
        "source": get_value(row, "me").title(),
        "destination": get_partner_text(row),
        "amount": parse_amount(get_value(row, "amount"), ","),
        "category": category
    }

def make_bank_transaction(row, label = "", category = ""):
    amount = parse_amount(get_value(row, "amount"), ",")
    if amount > 0:
        return make_bank_deposit(row, category)
    else:
        return make_bank_payment(row, category)

def write_bank_transactions(source, target):
    with open(source, "r", encoding="iso-8859-1") as input, open(target, "w+") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        reader = csv.DictReader(input, delimiter=";")
        writer.writeheader()
        next(reader)
        for row in reader:
            transaction = make_bank_transaction(row, category="Other")
            writer.writerow(transaction)