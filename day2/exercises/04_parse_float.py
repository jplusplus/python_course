# -*- coding: utf-8 -*-

""" ÖVNING:
	Skapa en lista med dictionaries, som ser ut så här:
	{
		"municipality": "Stockholm",
		"unemployment2014": 5.139667,
		"unemployment2013": 5.404515,
		"change": -0.264848,
		"sentence": "Din beskrivnade mening här...", 
	}
	Det här motsvarar en rad i den kommande csv-filen som vi kommer att skapa
"""

import csv
import locale

locale.setlocale(locale.LC_ALL, 'sv_SE')

file_name = "unemployment.csv"

# Öppnar filen
print("Öppnar %s" % file_name)
in_file = open(file_name, 'rb')
csv_file = csv.DictReader(in_file, delimiter=',')

# Funktion för att beskriva abretslösheten
def get_sentence(municipality, unemployment2014, unemployment2013):
	sentence = "Arbetslösheten i %s var år 2014 %s procent jämfört med %s år 2013." % (municipality, unemployment2014, unemployment2013)
	return sentence

data = []
for line in csv_file:
	""" Övning
	"""
	print line