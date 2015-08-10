# -*- coding: utf-8 -*-

import csv

file_name = "unemployment.csv"

# Öppnar filen
print "Öppnar %s" % file_name
csv_file = csv.DictReader(open(file_name, 'rb'), delimiter=',')

""" ÖVNING:
	Återanvänd koden från föregående övning, men paketera den som en funktion.
	Loopa genom csv-filen och använd textfunktionen för att skriva meningar. 
"""

def write_sentence(municipality, unemployment2014, unemployment2013):
	# Din kod här
	print "En dynamisk mening"

for line in csv_file:
	print line