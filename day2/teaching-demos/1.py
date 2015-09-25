# coding: utf-8

import joachimmail
import csv

mep_file = open("meps.csv")
meps = csv.DictReader(mep_file)

for mep in meps:
    joachimmail.emailify(mep['namn'], "riksdagen.se")
