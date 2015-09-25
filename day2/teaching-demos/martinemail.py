#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""


def emailify(name, domain):
    formated_name = name.lower()\
        .replace(" ", ".")\
        .replace("å", "a")\
        .replace("ä", "a")\
        .replace("ö", "o")\
        .replace("é", "e")\
        .replace("Ö", "o")

    email = formated_name + domain
    print(email)
