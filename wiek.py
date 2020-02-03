# #! /usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# # deklarujemy i inicjalizujemy zmienne
#
# pythonRok = 1989
#
# # pobieramy dane
# aktRok = int(input('Podaj aktualny rok'))
# imie = input('Jak się nazywasz? ')
# wiek = int(input('Ile masz lat? '))
#
# # obliczamy wiek Pythona
# wiekPythona = aktRok - pythonRok
#
#
#
#
# # wyświetlamy komunikaty
# print("Witaj", imie)
# print("Mów mi Python, mam", wiekPythona, "lat.")
#
# # instrukcja warunkowa
# if wiek > wiekPythona:
#     print('Jesteś starszy ode mnie o ', wiek-wiekPythona)
# else:
#     print('Jesteś młodszy ode mnie o ', -wiek+wiekPythona)


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

op = "n"
while op == "n":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")

    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmniejsza:")

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    op = input("Jeszcze raz (t/n)? ")

print("Koniec.")
