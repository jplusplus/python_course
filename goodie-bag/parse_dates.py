# -*- coding: utf-8 -*-
""" Tolka datum i format som förekommer i svenska myndighetstexter
"""
import re

datePatterns = [
    '((19|20)\d{2}-\d{1,2}-\d{1,2})',  # 2014-03-24 och 2014-3-24
    '((19|20)\d{2}/\d{1,2}/\d{1,2})',  # 2014/03/24 ich 2014/3/24
    '(\d{1,2}\.\d{1,2}\.(19|20)\d{2})',  # 24.3.2014
    '(\d{1,2}\s(januari|februari|mars|april|maj|juni|juli|augusti|september|oktober|november|december)\s(19|20)\d{2})',  # 24 mars 2014
    '(\d{1,2}\s(jan|feb|mar|apr|jun|jul|aug|sep|okt|nov|dec)\.?\s?(19|20)\d{2})']  # 24 mar 2014, 24 mar. 2014, 24 mar.2014
"""
 ”Myndigheternas skrivregler” rekommenderar '2005-05-24' eller '24.5.2005',
 men även '24 mars 2014'  och '24 mar 2014' är relativt vanligt förekommande.
"""

earliest_date = "1970-01-01"
"""
 För att underlätta tolkningen av luddiga datum (10-04-03),
 så anger vi ett tidigast möjliga datumet vi tror att vi stöter på här."""


def replace_set(text, dictionary):
    """ Ersätter en uppsättning tecken eller strängar med en annan.
    """
    import re

    rep = dict((re.escape(k), v) for k, v in dictionary.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], text)


def _parse_date(date, after):
    """ Omvandlar en textsträng till ett datumformat """
    import dateutil.parser as dateParser
    from datetime import datetime
    month_dict = {u"januari": u"January",
                  u"februari": u"February",
                  u"mars": u"March",
                  u"april": u"April",
                  u"maj": u"May",
                  u"juni": u"June",
                  u"juli": u"July",
                  u"augusti": u"August",
                  u"september": u"September",
                  u"oktober": u"October",
                  u"november": u"November",
                  u"december": u"December",
                  u"okt": u"October"}
    date_string = replace_set(date, month_dict)

    try:
        parsed_date = dateParser.parse(date_string,
                                       fuzzy=True,
                                       ignoretz=True,  # No timezones used
                                       yearfirst=True,  # 2014-03-24
                                       dayfirst=True)  # 24.3.2014
        now = datetime.now()
        after_date = datetime.strptime(after, "%Y-%m-%d")
        if (parsed_date > now) or (parsed_date < after_date):
            parsed_date = None
    except ValueError:
        parsed_date = None
    return parsed_date


def get_dates(text):
    dates = []
    for pattern in datePatterns:
        datestrings = re.compile(pattern).findall(text)
        dates.extend([_parse_date(x[0], earliest_date) for x in datestrings])
    return dates


print(get_dates("I dag är det den 6 maj 2015"))
print(get_dates("2015-10-02 och 2015-10-03"))
