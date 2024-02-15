# Opdracht 1 berekeningen
# Naam student: Ina
# Groep: ITX1

#define the dictionary with three friends and their respective ages
friends = {"Paulo":21, "Jacq":29, "Sam":18}
#define an empty list for the ages for calculations
ages = []

#print some text
print("LEEFTIJDEN:")
for i in friends:
    #for every friend in the dictionary, print the friend's name and their respective age
    print(i+": "+str(friends[i]))
    #add the friend's age to the ages list
    ages.append(friends[i])

#print the sum of all ages in the ages list
print("Het totaal van alle leeftijden is "+str(sum(ages)))
#print the mean of all ages in the ages list
print("Het gemiddelde van alle leeftijden is "+str(round(sum(ages)/len(ages), 2)))
