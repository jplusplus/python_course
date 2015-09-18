# coding: utf-8
"""
 Skriv en nyhetsrubrik

"""

population2012 = 9500000
population2013 = 9600000
diff = population2013 - population2012

if population2013 > population2012:
    heading = "Sveriges befolkning ökar"
if population2013 < population2012:
    heading = "Sveriges befolkning allt mindre"

print(heading)
