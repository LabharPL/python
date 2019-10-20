# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import random
# #
# # liczba = random.randint(1, 10)
# #
# #
# # odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
# #
# # if int(odp) == liczba:
# #     print("Zgadłeś")
# #
# # print("Wylosowana liczba:", liczba)
# #
# # print("Twoja liczba:", odp)
#
#
# ileliczb = int(input("podaj ile liczb lodusjesz?"))
#
# maksliczba = int(input("podaj max liczbę z jakich będziesz losował"))
# print("wylosujesz  ",ileliczb," z ", maksliczba)
# print(maksliczba)
# print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
# liczby = []
# # for i in range(ileliczb):
# i = 0
# while i < ileliczb:
#     liczba = random.randint(1, maksliczba)
#
#     if liczby.count(liczba) == 0:
#         liczby.append(liczba)
#         i = i + 1
#
# print("Wylosowane liczby:", liczby)
#
#
# print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
# typy = set()
# i = 0
# while i < ileliczb:
#     typ = int(input("Podaj liczbę %s: " % (i + 1)))
#     if typ not in typy:
#         typy.add(typ)
#         i = i + 1
#
#
# print(liczby, ' typy ', typy)
#
# trafione = set(liczby) & typy
# if trafione:
#     print("\nIlość trafień: %s" % len(trafione))
#     print("Trafione liczby: ", trafione)
# else:
#     print("Brak trafień. Spróbuj jeszcze raz!")





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

try:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb > maksliczba:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

for i in range(3):
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

print("Wylosowane liczby:", liczby)