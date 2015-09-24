# -*- coding: utf-8 -*-

"""	Övning öppna en lista med csv
"""

import urllib2
import lxml

url = 'http://jplusplus.se/'
response = urllib2.urlopen(url)
html = response.read()
