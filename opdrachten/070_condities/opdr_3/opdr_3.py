# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

visitor_age = int(input("Geef uw leeftijd in jaren: "))

for age in leeftijd:
    if visitor_age >= leeftijd[age][0] and visitor_age <= leeftijd[age][1]:
        korting = normale_toegangsprijs-(normale_toegangsprijs * kortings_percentages[age])/100
        print(f"U behoort tot de groep {age}")
        print(f"U krijgt {kortings_percentages[age]}% korting")
        print(f"U betaald dus {korting}")
