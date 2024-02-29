# Opdracht 4 condities
# Naam student:
# Groep:



toppings = {"olijven": 4.50, "kaas": 3.50, "salami": 3.00, "pepperoni": 2.00 , "ansjovis": 2.50}
beschikbare_toppings = list(toppings.keys())

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")
if keuze.lower() in beschikbare_toppings:
    print(f"U heeft {keuze} besteld. Dat kost {toppings[keuze]}")
else:
    print("Uw keuze zit niet in ons assortiment")