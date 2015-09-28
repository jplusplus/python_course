# coding: utf-8 

"""
HEMUPPGIFT 1
============
Hur många riksdagsledamöter har ett son-namn?

1) Loopa listan med riksdagsledamöter
2) Kolla om personen har ett "son"-namn
3) Räkna många riksdagsledamöter som har son-namn.

Bonus: Räkna hur stor andel av ledamöterna i varje parti som har son-namn. 
"""

""" 
Vi hämtar listan med data från en extern fil här (riksdagsledamoter.py).
I praktiken är det exakt samma sak som när vi i 02c_for_loops.py definierade 
data = [
    {"municipality": "Ale",
     "unemployment_2009": 5.5,
     "unemployment_2014": 4.9
    },
    ...
]

"""
from riksdagsledamoter import data

counter_son_names = 0
total_number_of_mps = len(data)

for row in data:
    print(row)
    # Skriv kod här!

print("Av %s riksdagsledamöter har %s son-namn" % (total_number_of_mps, counter_son_names))