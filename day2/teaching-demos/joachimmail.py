# -*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""


def emailify(name, domain):
    name_list = name.split(" ")
    new_name = ".".join(name_list)
    small_name = new_name.lower()
    english_name = small_name\
        .replace("ö", "o")\
        .replace("ä", "a")\
        .replace("å", "a")\
        .replace("ü", "u")\
        .replace("é", "e")\
        .replace("É", "e")\
        .replace("Ö", "o")\
        .replace("Å", "a")\
        .replace("Ä", "ä")
    mail_address = english_name + "@" + domain
    print(mail_address)
