# Opdracht 2 lists
# Naam student: Ina
# Groep: ITX1


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

#Print de naam van de 1e rivier
print(rivieren[0].capitalize())

# Print het 2e land waar de 1e rivier doorheen stroomt
# Zowel land als rivier beginnen met een hoofdletter, gebruik hiervoor een tekstfunctie.
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

#Print de naam van de 1e rivier
print(rivieren[1].capitalize())

# Print het 2e land waar de 1e rivier doorheen stroomt
# Zowel land als rivier beginnen met een hoofdletter, gebruik hiervoor een tekstfunctie.
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")

#Print de naam van de 1e rivier
print(rivieren[2].capitalize())

# Print het 2e land waar de 1e rivier doorheen stroomt
# Zowel land als rivier beginnen met een hoofdletter, gebruik hiervoor een tekstfunctie.
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")
