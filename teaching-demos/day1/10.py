# coding: utf-8
"""
 Övning: Skriv ut arbetslösheten

"""


befolkning = 6058.1  # tusental
arbetslosa = 424.8
ej_i_arbetskraft = 986.6
sysselsatta = 4646.6

andel_sysselsatta = sysselsatta / befolkning

arbetsfor_befolkning = befolkning - ej_i_arbetskraft
arbetsloshet = arbetslosa / arbetsfor_befolkning

print("Andelen sysselsatta är %s procent och arbetslösheten %s procent" % (andel_sysselsatta * 100, arbetsloshet * 100))
