# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
items=[]

for i in range(0, 5):
    items.append(input("Enter an object to add to the item list: "))

print(sorted(items, key=str.lower, reverse=True))
