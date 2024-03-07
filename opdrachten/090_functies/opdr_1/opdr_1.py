# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(filex, texty):
    fo = open(filex, "a")
    fo.write(texty+"\n")
    pass

my_tekst = input("What text would you like to add to the file?\n")
my_file = input("What is the file name?\n")+".txt"
write_to_file(my_file, my_tekst)
