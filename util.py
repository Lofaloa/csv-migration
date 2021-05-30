import datetime as d

def parse_amount(amount_str, decimal_sep = ".", deletechars = " €+"):
    if type(amount_str) is str:
        for char in deletechars:
            amount_str = amount_str.replace(char, "")
        if decimal_sep == ",":
            amount_str = amount_str.replace(decimal_sep, ".")
        return float(amount_str)
    else:
        raise TypeError("Invalid amount type.")

def clean_date(date_str, format = "%d-%m-%Y"):
    if type(date_str) is str:
        return d.datetime.strptime(date_str, format).date().isoformat()
    else:
        raise TypeError("Invalid date type.")