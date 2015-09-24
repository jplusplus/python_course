# -*- coding: utf-8 -*-

""" ÖVNING:

"""

import csv
import locale

locale.setlocale(locale.LC_ALL, "sv_SE")

# Filernas namn
in_file_name = "unemployment.csv"
out_file_name = "unemployment_with_sentence.csv"

# Öppna in- och ut-filerna
in_file = open(in_file_name, 'rb')
out_file = open(out_file_name, 'wb')

# Läs in in-filen
csv_in_file = csv.DictReader(in_file, delimiter=',')
csv_out_file = csv.DictWriter(out_file,
                              delimiter=',',
                              fieldnames=["name",
                                          "2014", "2013",
                                          "change", "sentence"]
                              )


# Funktion för att skriva en mening som beskriver abretslösheten
def get_sentence(municipality, unemployment2014, unemployment2013):
    sentence = "Arbetslösheten i %s var år 2014 %s procent jämfört med %s år 2013." % (municipality, unemployment2014, unemployment2013)
    return sentence

data = []
for line in csv_in_file:
    new_line = {}
    new_line["name"] = line["Kommun"]
    new_line["2014"] = locale.atof(line["2014"])
    new_line["2013"] = locale.atof(line["2013"])
    new_line["change"] = new_line["2014"] - new_line["2013"]
    new_line["sentence"] = get_sentence(new_line["name"],
                                        new_line["2014"],
                                        new_line["2013"])
    csv_out_file.writerow(new_line)
