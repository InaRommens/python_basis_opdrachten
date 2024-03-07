# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier


def questions():
    qresults = []
    qresults.append(input("Wat vind je van de huidige regering?\n"))
    qresults.append(input("Wat vind je van de Python-lessen tot nu toe?\n"))
    qresults.append(input("Wat vind jij de mooiste stad van Nederland?\n"))
    return qresults


def write_out(content):
    fo = open("QuestionResults.txt", "wt")
    for i in content:
        fo.write(i + "\n")
    fo.close()
    return


def main():
    write_out(questions())
    return

main()