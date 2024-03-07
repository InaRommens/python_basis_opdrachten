# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


def questions():
    vragenlijst = ["Wat is je voornaam?\n",
                   "Wat is je achternaam?\n",
                   "Wat neem je mee aan drank?\n",
                   "Wat neem je mee om te eten?\n"]
    antwoordenlijst = []
    answer_keys = ["voornaam", "achternaam", "drank", "eten"]
    answers = {}

    for i in vragenlijst:
        antwoordenlijst.append(input(i))

    for i in range(0, 4):
        answers[answer_keys[i]] = antwoordenlijst[i]

    return answers


def main():
    inputmode = True
    fo = open("BYOB.txt", 'a')

    while inputmode:
        inputF = input("Would you like to enter another guest? (enter 'q' to exit input mode)\n")
        if inputF == "q":
            inputmode = False
            fo.close()
            continue
        output = questions()
        for i in output:
            fo.write(f"{i}: {output[i]}\n")
        fo.write("\n")
    return


if __name__ == '__main__':
    main()