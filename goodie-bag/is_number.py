# coding: utf-8

"""
Två funktioner för att
a) Kolla om en textsträng är ett decimaltal.
b) Göra om en textsträng till ett decimaltal om möjligt.

Båda funktionerna klarar av att hantera både punkt och komma som decimaltecken,
men de hanterar inte tusentalsavgränsare.
"""


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        try:
            float(string.replace(",", "."))
            return True
        except ValueError:
            return False
    except TypeError:
        return False


def parse_float(string):
    """Gör om en sträng till ett tal"""
    string = string.strip().replace(" ", "")
    try:
        return float(string)
    except ValueError:
        return float(string.replace(",", "."))


print(is_number("1234"))
print(is_number("1234.5"))
print(is_number("1234,5"))
print(is_number("abc1234.5w"))

print(parse_float("1234"))
print(parse_float("1234.5"))
print(parse_float("1 234,5"))
