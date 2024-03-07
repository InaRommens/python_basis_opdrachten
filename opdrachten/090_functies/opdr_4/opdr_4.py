# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for i in lijst_met_namen:
        naam = ""
        for j in i:
            if i[j]:
                naam += i[j]+" "
        print(naam)
    pass


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)