# coding: utf-8
"""
 Övning: Skriv en e-postadress, II
"""
name = "Stefan Löfven"
domain = "riksdagen.se"

email_friendly_name = name.lower()
email_friendly_name = email_friendly_name.replace(" ", ".")
email_friendly_name = email_friendly_name.replace("å", "a").replace("ä", "a").replace("ö", "o")

email = email_friendly_name + "@" + domain
print email
