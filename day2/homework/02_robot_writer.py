# coding: utf-8 

"""
HEMUPPGIFT 2
============
Skriv 290 notiser om arbetslösheten!

Jobba vidare på funktionen du skrev i förra hemläxan som skrev en 
nyhetstext om arbetslöshetsutvecklingen i en kommun.
Den här gången ska du skriva notiser om ALLA kommuner genom att loopa
genom en kommunlista.

BONUS:
Utveckla din write_story()-funktion så att den också 
använder categorize_unemployment() som vi skrev under lektionen.
"""

"""
Hämta in en lista med kommundata från filen unemployment.py
"""
from unemployment import data

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

""" Klistra in din egen write_story-funktion här
"""
def write_story(municipality, unemployment_2009, unemployment_2014):
    story = "Skriv en story!"

for row in data:
    print row
    # Skriv kod här!