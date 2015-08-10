# -*- coding: utf-8 -*-


"""
Hemuppgift:
===========

Skapa en funktion som tar arbetslöshetsprocenten för en viss månad vid två givna år och skriver ut en kort notis.
En notis kan se ut ungefär så här:
	
	Arbetslösheten i maj var 1,3 procentenheter högre än vid motsvarande tidpunkt i fjol.
	7,5 procent av alla arbetsföra saknade jobb, jämför med 6,2 i maj 2014.

Textroboten måste vara beredd på att arbetslösheten kan öka, minska eller vara oförändrad.
Vill man göra roboten lite mer avancerad kan man låta den ta hänsyn till förändringens storlek: "Arbetslösheten steg med HELA 2,3 procentenheter"
"""

def write_story(year0, unemployment0, year1, unemployment1, month):
	# Skriv kod här!



""" Testa roboten!
"""

write_story(2014, 9.2, 2015, 8.5, "juni") 
print "**************"

write_story(2008, 5.9, 2009, 9.0, "november") 
print "**************"

write_story(2013, 8.7, 2014, 8.7, "april") 
print "**************"

"""
Källa: http://www.ekonomifakta.se/sv/Fakta/Arbetsmarknad/Arbetsloshet/Arbetsloshet/
"""