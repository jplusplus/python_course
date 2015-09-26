# -*- coding: utf-8 -*-

""" Se robot_writer.md för instruktioner
"""

total_unemployment_2014 = 8.0
total_unemployment_2009 = 5.9


def write_story(municipality, unemployment_2009, unemployment_2014):
    neg_text=("I "+municipality+" gar var %s:e utan jobb" %int(round(100/unemployment_2014)) +"\n"+ 
        "Arbetslosheten i "+municipality+" var forra aret %s procent. " %unemployment_2014+
        "Det ar %s procentenheter hogre an i riket som helhet." %abs(total_unemployment_2014-unemployment_2014)+
        "Pa fem ar har arbetslosheten i "+municipality+" okat med %s procenenheter." %(unemployment_2014-unemployment_2009))

    pos_text=(municipality+" klarar sig bra"+"\n"+
        "I "+municipality+" var arbetslosheten %s procent under 2014. " %unemployment_2014+
        "Jamfort med 2009 ar det en minskning med %s procentenheter. " %abs(unemployment_2014-unemployment_2009)+
        "Arets siffra ar %s procentenheter lagre an den totala arbetslosheten forra aret." %(total_unemployment_2014-unemployment_2014))

    mkt_pos_text=("Supersiffror for "+municipality+"\n"+
        municipality+"s arbetsloshet var %s procent under 2014. " %unemployment_2014+
        "Det ar hela %s procentenheter lagre an totalsiffran for Sverige. " %(total_unemployment_2014-unemployment_2014)+
        "Arbetslosheten i "+municipality+" har sjunkit med %s procentenheter sedan 2009." %(unemployment_2009-unemployment_2014))


    if (total_unemployment_2014-unemployment_2014)>=3.0:
        print(mkt_pos_text)

    else:
        if (total_unemployment_2014-unemployment_2014)<0.0:
            print(neg_text)

        if (total_unemployment_2014-unemployment_2014)>0.0:
            print(pos_text)