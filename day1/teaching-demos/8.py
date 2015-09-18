# coding: utf-8
"""
 Övning: Skriv en e-postadress

"""

first_name = "gustaf"
last_name = "fridolin"
domain = "riksdagen.se"

email = first_name + "." + last_name + "@" + domain
print(email)

email = "%s.%s@%s" % (first_name, last_name, domain)
