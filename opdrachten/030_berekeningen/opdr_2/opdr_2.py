# Opdracht 2 berekeningen
# Naam student: Ina
# Groep: ITX1

# define the function to convert celsius and fahrenheit
def conv_t(c=None, f=None):
    while c:
        conv_f = str(round((c * (9 / 5)) + 32, 2))
        print(str(c) + " graden celsius is gelijk aan " + conv_f + " graden fahrenheit")
        c = None
    while f:
        conv_c = str(round((f - 32) * (5 / 9), 2))
        print(str(f) + " graden fahrenheit is gelijk aan " + conv_c + " graden celcius")
        f = None


def main():
    conv_t(c=-12, f=122)
    conv_t(c=62.2, f=96)
    exit()


if __name__ == '__main__':
    main()
