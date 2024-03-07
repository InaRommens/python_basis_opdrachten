#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

def get_csv(filename):
    open_file = []
    for l in open(filename, 'rt'):
        clean_line = []
        line = l.split(",")
        for e in line:
            clean_line.append(e.lower().rstrip().strip())
        open_file.append(clean_line)
    return open_file


def create_entries(data):
    processed = []
    for e in data:
        entry = {"voornaam": e[0].title(), "tussenvoegsel": e[1], "achternaam": e[2].title(),
                 "adres": e[3].title(), "postcode": e[4].upper(), "plaats": e[5].title()}
        if e[1]:
            entry["volle naam"] = f"{e[0].title()} {e[1]} {e[2].title()}"
        else:
            entry["volle naam"] = f"{e[0].title()} {e[2].title()}"
        processed.append(entry)
    return processed


def show_all(entries):
    counter = 0
    for e in entries:
        counter += 1
        print(f"VOLLEDIGE NAAM: {e["volle naam"]}\n"
              f"ADRES: {e["adres"]}, {e["postcode"]}, {e["plaats"]}\n")
    print(f"TOTAL ENTRIES SHOWN: {counter}\n")
    pass


def show_limited(entries, limits=["volle naam"]):
    counter = 0
    for e in entries:
        counter += 1
        for limit in limits:
            print(f"{limit.upper()}: {e[limit]}")
    print(f"TOTAL ENTRIES SHOWN: {counter}\n")
    pass


def show_filtered(entries, limit="volle naam", filter=""):
    counter = 0
    for e in entries:
        if filter.lower() in e[limit].lower():
            print(f"VOLLEDIGE NAAM: {e["volle naam"]}\n"
                  f"ADRES: {e["adres"]}, {e["postcode"]}, {e["plaats"]}\n")
            counter += 1
    print(f"TOTAL ENTRIES SHOWN: {counter}\n")
    pass