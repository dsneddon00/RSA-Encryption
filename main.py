#! /usr/bin/env python3
import math
import random
import primeMiller
from math import gcd as bltinGCD
import sys
import os


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

letter = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


public = "public.txt"
private = "private.txt"
#ASCII_MIN = 65;

class RSA:

    def __init__(self):
        return

    def GenerateKeys(self, longOne, longTwo):
        p = makePorQ(base26LetterToBase10(longOne.lower()))

        q = makePorQ(base26LetterToBase10(longOne.lower()))

        n = p * q

        r = (p - 1) * (q - 1)

        ok = False
        while ok != True:
            while ok != True or tmp > n:
                tmp = randomPower(398)
                ok = isCoPrime(tmp, r)
            e = tmp
            d = inverseMod(e, r)
            if d == False:
                ok = False
        print(f"len(p) : {len(str(p))}")
        print(f"len(q) : {len(str(q))}")
        print(f"len(n) : {len(str(n))}")
        print(f"len(r) : {len(str(r))}")
        print(f"len(e) : {len(str(e))}")
        print(f"len(d) : {len(str(d))}")

        if os.path.exists(public):
            os.remove(public)

        puF = open(public, "w")
        puF.write(str(n) + "\n")
        puF.write(str(e) + "\n")
        puF.close()

        if os.path.exists(private):
            os.remove(private)

        prF = open(private, "w")
        prF.write(str(n) + "\n")
        prF.write(str(d) + "\n")
        prF.close()


        '''
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

        l = greatestCommonFactor(r, k)

        while l != 1:
            k = k + 2
            l = greatestCommonFactor(r, k)

        e = k

        # private key
        d = inverseMod(e, r)

        fout = open("public.txt", "w")
        fout.write(str(n) + "\n")
        fout.write(str(e))
        fout.close()

        fout = open("private.txt", "w")
        fout.write(str(n) + "\n")
        fout.write(str(d))
        fout.close()
        '''


        return

    def Encrypt(inputFileName, outputFileName):
        # reading in binary mode
        fin = open(inputFileName, "rb")
        ptb = fin.read()
        pt = ptb.decode("utf-8")

        counter = 0
        fullList = []

        for i in range(len(pt)):
            counter += 1
            if(len(str(ALPHABET_INDEX[pt[i]])) <= 2):
                fullList.append(ALPHABET_INDEX[pt[i]])
            elif counter == 2:
                x = ALPHABET_INDEX[pt[i - 1]]
                fullList.append(int(str(x) + str(ALPHABET_INDEX[pt[i]])))
                fullList.remove(x)
                counter = 0
            else:
                fullList.append(ALPHABET_INDEX[pt[i]])
        fin.close()

        fin = open('public.txt', 'r')
        lines = fin.readlines()
        n = lines[0].strip()
        e = lines[1].strip()
        out = []

        for i in range(len(lst)):
            c = pow(int(lst[i]), int(e), int(n))
            out.append(c)
        fin.close()

        fout = open(outputFileName, "wb")
        for i in range(len(out)):
            line = str(output[i]) + "$"
            fout.write(line.encode("utf-8"))
        fout.close()


        return

    def Decrypt(inputFileName, outputFileName):
        fin = open(inputFileName, "rb")
        ptb = fin.read()
        pt = ptb.decode("utf-8")
        fullList = []
        fullList = [s.replace("$", ",") for s in pt]

        x = ""

        for i in range(len(fullList)):
            x += str(fullList[i])
        x = x[:-1]
        x = x.split(",")
        fin.close()


        fin = open("private.txt", "r")
        lines = fin.readlines()
        n = lines[0].strip()
        d = lines[1].strip()

        out = []
        outF = []

        for i in range(len(x)):
            m = pow(int(x[i]), int(d), int(n))
            out.append(m)
        finalOut = []

        for i in range(len(out)):
            outF.append(str(out[i]))

        for i in range(len(outF)):
            finalOut.append(str(ALPHABET[int(outF[i]) - 1]))

        fin.close()

        fout = open(outputFileName, "wb")
        for i in range(len(finalOut)):
            line = str(finalOut[i])
            fout.write(line.encode("utf-8"))
        fout.close()


        return


def base10ToLetter(number):
    if(number <= 0):
        # invalid
        return ""
    elif(number <= 26):
        return chr(96 + number)
    else:
        #run recursively
        return base10ToBase26Letter(int((number - 1) / 26)) + chr(97 + (num - 1) % 26)

def alphabetToBase10(statement, alphabet):
    total = 0
    for s in statement:
        counter = alphabet.find(s)
        if counter != -1:
            #thus being valid
            counter *= len(alphabet)
            counter += i

def base10ToAlphabet(number, alphabet):
    result = []
    n = num
    base = len(alphabet)
    c = 0
    while(n != 0):
        lst.insert(c, n % base)
        c = c // base
        c += 1

    # flip our list
    statement = ""
    result.reverse()

    for item in result:
        statement += alphabet[a]

    return statement

def randomPower(x):
    start = 10**(x - 1)
    end = (10**x) - 1
    return random.randint(start, end)


def greatestCommonFactor(x, y):
    while(y):
        x, y = y, x % y
    return x

def isCoPrime(x, y):
    m = min(x, y)

    for i in range(1, m + 1):
        if(x % i == 0 and y % i == 0):
            gcf = i
        if(gcf == 1):
            return True
        else:
            return False

def base26LetterToBase10(statement):
    statement = statement.lower()
    if statement == " " or len(statement) == 0:
        return 0
    if len(statement) == 1:
        # print(ord(string))
        return ord(statement)-96
    else:
        return base26LetterToBase10(statement[1:]) + (26 ** (len(statement)-1)) * (ord(statement[0]) - 96)

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
        return False
    else:
        return a % m

def invertInt(x):

    reverse = 0
    while(x > 0):
        d = x % 10
        reverse = reverse * 10 + d
        x = x // 10
    return reverse

def coPrime2(x, y):
    return (bltinGCD(x, y) == 1)

def makePorQ(number):

    if len(str(number)) < 200:
        print("the text is too short!\n")
        print(number)
        print(10**200)
        sys.exit(1)

    cut = number % pow(10, 200)

    if cut % 2 == 0:
        cut += 1

    while(primeMiller.isPrime(cut, 20) == False):
        cut += 2

    return cut

def main():
    sampleRSA = RSA()

    testing = "uibfasdoifubaoiusfdbiousadbfpiadubfoiaubfoiuabdoifubasdfoiubadfiobdfoiuadfoiubadfidsuabfoiadsubfaiodubdsafasdfafnoiujwasidufbiusbfdioaubfoidubfoiubdsfoiabudfoiuabdfiosbusaouidfs"
    testingTwo = "jbfoigboiadoidajnfijawndfioabwdiofdsufihsnoifjbeoijfbodjbdoifuabdifbaidfbaioudfboiasjbdfiuawbfeiowbfoejbfoiqeubfoiuqebofiuqebfasbdufbsiuadfubioaufbdoiafubdosifabuoisudbfoiasudbfoiadusbfoiausbdfioausbdfoisaubdf"

    sampleRSA.GenerateKeys(testing, testingTwo)

    return


if __name__ == "__main__":
    main()
