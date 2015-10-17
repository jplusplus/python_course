# coding: utf-8
"""
 ASCII är den teckenuppsättning som användes i datorernas barndom,
 och som fortfarande är en vanlig begränsning i e-postadresser
 och webbadresser
 https://en.wikipedia.org/wiki/ASCII

 För en utförligare lista över latinska tecken, se
 https://en.wikipedia.org/wiki/List_of_Latin-script_letters
"""


def asciify(string):
    """
     Ersätt vanliga latiska tecken med visuellt liknande ascii-
     tecken, som ofta används som ersättare i e-postadresser
     och liknande.
    """
    replacements = [("å", "a"), ("ä", "a"), ("ö", "o"),
                    ("Å", "a"), ("Ä", "a"), ("Ö", "o"),
                    ("é", "e"), ("È", "e"), ("È", "E"), ("è", "e"),
                    ("Ë", "E"), ("ë", "e"), ("Ê", "E"), ("ê", "e"),
                    ("ü", "u"), ("Ü", "u"),
                    ("Š", "S"), ("š", "s"), ("Ž", "Z"), ("ž", "z")
                    ("Œ", "OE"), ("œ", "oe"),
                    ("Ÿ", "Y"), ("ÿ", "y"),
                    ("À", "A"), ("à", "a"), ("Á", "A"), ("á", "a"),
                    ("Â", "A"), ("â", "a"), ("Ã", "A"), ("ã", "a"),
                    ("Æ", "Ä"), ("æ", "ä"),
                    ("Ç", "C"), ("ç", "c"),
                    ("Í", "I"), ("í", "i"), ("Ì", "I"), ("ì", "i"),
                    ("İ", "I"), ("ı", "i"),
                    ("Ó", "O"), ("ó", "o"), ("Ò", "O"), ("ò", "o"),
                    ("Õ", "O"), ("õ", "o"), ("Ô", "O"), ("ô", "o"),
                    ("Ú", "U"), ("ú", "u"), ("Ù", "U"), ("ù", "u"),
                    ("Û", "u"), ("û", "u"),
                    ("Ð", "D"), ("ð", "d"),
                    ("Ñ", "N"), ("ñ", "n"),
                    ("ß", "ss"),
                    ("Ø", "O"), ("ø", "o")
                    ]
    # Fler latinska tecken här:
    #  https://en.wikipedia.org/wiki/List_of_Latin-script_letters
    for replacement in replacements:
        string = string.replace(replacement[0], replacement[1])

    return string


def emailify(string):
    """
     Ersätt latinska tecken med de motsvarigheter som ofta
     används i e-postadresser
    """
    string = string.lower().replace(" ", ".")
    string = asciify(string)
    return string
