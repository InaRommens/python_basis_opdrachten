# Opdracht 1 modules
# Naam student:
# Groep:

from my_modules.csv import get_csv
from my_modules.csv import create_entries
from my_modules.csv import show_all
from my_modules.csv import show_limited
from my_modules.csv import show_filtered

entries = create_entries(get_csv("personen.csv"))
show_all(entries)
show_limited(entries, limits=["volle naam", "adres"])
show_filtered(entries, limit="adres", filter="k")



