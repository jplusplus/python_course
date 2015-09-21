# coding: utf-8
"""
 Övning: Räkna ut arbetslösheten

"""


befolkning = 6058.1  # tusental
arbetslosa = 424.8
ej_i_arbetskraft = 986.6
sysselsatta = 4646.6

andel_sysselsatta = sysselsatta / befolkning
print(andel_sysselsatta * 100)  # andel sysselsatta

arbetsfor_befolkning = befolkning - ej_i_arbetskraft
arbetsloshet = arbetslosa / arbetsfor_befolkning
print(arbetsloshet * 100)  # andelen arbetslösa av den arbetsföra befolkningen
