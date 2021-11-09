#! /usr/bin/env python3
import math
import random
import primeMiller


'''
 ____ ____ ____
||R |||S |||A ||
||__|||__|||__||
|/__\|/__\|/__\|
 ____ ____
||B |||y ||
||__|||__||
|/__\|/__\|
 ____ ____ ____ ____ ____
||D |||e |||r |||e |||k ||
||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ ____ ____ ____
||S |||n |||e |||d |||d |||o |||n ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

'''

# constants
ALPHABET = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ALPHABET_INDEX = {a: i for i, a in enumerate(ALPHABET, 1)}

#ASCII_MIN = 65;

class RSA:

    def __init__(self):
        return

    def GenerateKeys(longOne, longTwo):
        x = 0
        y = 0
        for c in longOne.upper():
            x = x * len(ALPHABET) + ALPHABET_INDEX[c]

        for c in longTwo.upper():
            y = y * len(ALPHABET) + ALPHABET_INDEX[c]

        modX = x % (pow(10, 200))
        modY = y % (pow(10, 200))

        if(len(str(x)) < len(str(modX)) or len(str(y)) < len(str(modY))):
            print("Check sizes")

        oddX = modX
        oddY = modY
        # check if not odd, if not, then make odd
        if ((oddX % 2) == 0):
            oddX = oddX + 1

        if((oddY % 2) == 0):
            oddY = oddY + 1

        # use our previous functions for prime miller stuff
        # if it's prime, we can add 2 to make it no longer prime
        while primeMiller.isPrimeMiller(oddX) != True:
            oddX = oddX + 2
        while primeMiller.isPrimeMiller(oddY) != True:
            oddY = oddY + 2

        # the p q algorithm that Bart talked about in class and I took notes on
        p = oddX
        q = oddY
        n = p*q
        r = (p - 1) * (q - 1)
        k = n - 1300


        return

    def Encrypt(inputFileName, outputFileName):
        return

    def Decrypt(inputFileName, outputFileName):
        return


#def base10ToAlphabet(number):


def greatestCommonFactor(x, y):
    while(y):
        x, y = y, x % y
    return x

# also known as egcd
def euclidean(x, y):
    if(x == 0):
        return (y, 0, 1)
    else:
        # call recursively
        g, a, b = euclidean(y % x, x)
        return (g, b - (y // x) * a, a)

def inverseMod(x, m):
    g, a, b = euclidean(x, m)
    if g != 1:
        raise Exception("No Inverse Mod")
    else:
        return a % m


def main():
    return


if __name__ == "__main__":
    main()
