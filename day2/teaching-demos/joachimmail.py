# -*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""


def emailify(name, domain):
    name_split = name.split()
    first_name = name_split[0]
    last_name = name_split[1]
    name = first_name + "." + last_name
    small_name = name.lower()
    english_name = small_name.replace("ö", "o").replace("ä", "a").replace("å", "a").replace("é", "e").replace("Ö", "o")
    mail_address = english_name + "@" + domain
    print(mail_address)
