# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


def encrypt(texty):
    text_e = []
    no_enc = [" ", ",", ".", "!", "?", "\'", "\""]

    for i in texty.lower():
        if i in no_enc:
            text_e.append(i)
            continue
        text_e.append(chr((ord(i)+5-97) % 26 + 97))

    return ''.join(text_e)


def main():
    encrypted = encrypt(input("What would you like to encrypt?\n")).capitalize()
    print(encrypted)

if __name__ == '__main__':
    main()