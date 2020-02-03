# #! /usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import math  # dołączamy bibliotekę matematyczną
#
# op = "t"  # deklarujemy i inicjujemy zmienną pomocniczą
# while op != "n":  # dopóki wartość zmiennej op jest inna niż znak "n"
#     dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")
#
#     # lista = []  # definicja pustej listy
#     # for x in dane.split(","):
#     #     lista.append(int(x))  # dodanie lementu do listy
#     # a, b, c = lista  # rozpakowanie listy
#     # wyrażenie listowe, które zastępuje kod 10-13:
#     a, b, c = [int(x) for x in dane.split(",")]
#
#     print("Podano boki: ", a, b, c)
#
#     if a + b > c and a + c > b and b + c > a:  # warunek złożony
#         print("Z podanych boków można zbudować trójkąt.")
#         # czy boki spełniają warunki trójkąta prostokątnego?
#         if (a**2 + b**2 == c**2 or
#                 a**2 + c**2 == b**2 or
#                 b**2 + c**2 == a**2):
#             print("Do tego prostokątny!")
#
#         # na wyjściu możemy wyprowadzać wyrażenia
#         print("Obwód wynosi:", (a + b + c))
#         p = 0.5 * (a + b + c)  # obliczmy współczynnik wzoru Herona
#         # liczymy pole ze wzoru Herona
#         P = math.sqrt(p * (p - a) * (p - b) * (p - c))
#         print("Pole wynosi:", P)
#         op = "n"  # ustawiamy zmienną na "n", aby wyjść z pętli while
#     else:
#         print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
#     op = input("Spróbujesz jeszcze raz (t/n): ")
#
# print("Do zobaczenia...")



#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65, 119):
    litera = chr(i)
    x += 1
    tmp = str(i) + ">>" + litera + " => " + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")

x = -1
print("\nAlfabet w porządku odwróconym:")
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(litera.upper(), "=>", litera, end=" ")
#
# #! /usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# from random import randint
#
# ile = int(input("Ile liczb wylosować? "))
# lista = []  # pusta lista
# for i in range(0, ile):
#     lista.append(randint(0, 100))
# print(lista)
#
# print("Dodawanie elementów na końcu listy")
# for i in range(0, 3):
#     liczba = int(input("Podaj liczbę: "))
#     lista.append(liczba)
# print(lista)
#
# print("Zawartość listy ([indeks] wartość):")
# for i, v in enumerate(lista):
#     print("[", i, "]", v)
#
# print("Elementy w odwróconym porządku:")
# for e in reversed(lista):
#     print(e, end=" ")
#
# print()
# print("Elementy posortowane rosnąco:")
# for e in sorted(lista):
#     print(e, end=" ")
#
# print()
# e = int(input("Którą liczbę usunąć? "))
# lista.remove(e)
# print(lista)
#
# print("Wstawianie elementów do listy")
# a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
# lista.insert(i, a)
# print(lista)
#
# print("Wyszukiwanie i zliczanie elementu w liście")
# e = int(input("Podaj liczbę: "))
# print("Liczba wystąpień: ")
# print(lista.count(e))
# print("Indeks pierwszego wystąpienia: ")
# if lista.count(e):
#     print(lista.index(e))
# else:
#     print("Brak elementu w liście")
#
# print("Pobieramy ostatni element z listy: ")
# print(lista.pop())
# print(lista)
#
# print("Część listy (notacja wycinkowa):")
# i, j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: "))
# print(lista[i:j])
#
# print()
# print("Tupla to lista niemodyfikowalna.")
# print("Próba zmiany tupli generuje błąd:")
# tupla = tuple(lista)
# # tupla[0] = 100


#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def fib_iter1(n):  # definicja funkcji
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą while.
    """
    pwyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy  # przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ")
    while n > 1:
        print (b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1


def fib_iter2(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b


def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
        Wersja rekurencyjna.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)


def main(args):
    n = int(input("Podaj nr wyrazu: "))
    fib_iter1(n)
    print()
    print("=" * 40)
    fib_iter2(n)
    print("=" * 40)
    print(fib_rek(n - 1))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
