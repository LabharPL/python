#! /usr/bin/env python3
# -*- coding: utf-8 -*-

KLUCZ = 4
AREK = 26


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - AREK)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
        print(zaszyfrowny + '  ..  ')
        print('tekst długi na  '+str(len(zaszyfrowny)))
    return zaszyfrowny

def deszyfruj(tekstsz):
    odszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for znak in tekstsz:
        if (ord(znak) - KLUCZM < 97):
            odszyfrowany += chr(ord(znak) - KLUCZM + 26)
        else:
            odszyfrowany += chr(ord(znak) - KLUCZM)
    return odszyfrowany



def main(args):
    # AREK = input("podaj 26")
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    szyfrowany = szyfruj(tekst)
    # print(szyfrowany)
    print('odszyfrowany  ', deszyfruj(szyfrowany))
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
