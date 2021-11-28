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

    def GenerateKeys(self, loneOne, loneTwo):
        p = makePorQ(base26LetterToBase10(loneOne.lower()))
        q = makePorQ(base26LetterToBase10(loneTwo.lower()))
        n = p * q
        r = (p - 1) * (q - 1)
        ok = False
        while ok != True:
            while ok != True or tmp > n:
                tmp = randomPower(400)
                ok = isCoPrime(tmp, r)
            e = tmp

            d = inverseMod(e, r)
            if d == False:
                ok = False

        if os.path.exists(public):
            os.remove(public)

        pubF = open(public, "w")
        pubF.write(str(n) + "\n")
        pubF.write(str(e) + "\n")
        pubF.close()
        if os.path.exists(private):
            os.remove(private)
        priF = open(private, "w")
        priF.write(str(n) + "\n")
        priF.write(str(d) + "\n")
        priF.close()


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

    def Encrypt(self, inputFileName, outputFileName):
        print("Start Encrypt\n")
        pubF = open(public, "r") if os.path.exists(
            public) else sys.exit(1)
        lines = pubF.readlines()
        n = int(lines[0].replace("\n", ''))
        e = int(lines[1].replace("\n", ''))
        pubF.close()
        iFile = open(inputFileName, "rb") if os.path.exists(
            inputFileName) else sys.exit(1)
        if os.path.exists(outputFileName):
            os.remove(outputFileName)
        oFile = open(outputFileName, "wb")
        result = []
        for ptBinaray in iter(lambda: iFile.read(200), b''):
            pt = ptBinaray.decode("utf-8")
            alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            num = alphabetToBase10(pt, alphabet)
            c = pow(num, e, n)
            block = base10ToAlphabet(c, alphabet) + "$"
            result.append(block)

        oFile.write("".join(result).encode("utf-8"))
        iFile.close()
        oFile.close()

    def Decrypt(self, inputFileName, outputFileName):
        print("Start Decrypt\n")

        priF = open(private, "r") if os.path.exists(
            private) else sys.exit(1)
        lines = priF.readlines()
        n = int(lines[0].replace("\n", ''))
        d = int(lines[1].replace("\n", ''))
        priF.close()

        iFile = open(inputFileName, "rb") if os.path.exists(
            inputFileName) else sys.exit(1)

        if os.path.exists(outputFileName):
            os.remove(outputFileName)
        oFile = open(outputFileName, "wb")

        encryptedBlocks = iFile.read().decode("utf-8").split("$")
        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result = []
        for block in encryptedBlocks:
            if block != '':
                c = alphabetToBase10(block, alphabet)
                m = pow(c, d, n)
                print(m)
                text = base10ToAlphabet(m, alphabet)
                print(text)
                result.append(text)

        oFile.write("".join(result).encode("utf-8"))

        iFile.close()
        oFile.close()


        '''
        fin = open(inputFileNameName, "rb")
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

        fout = open(outputFileNameName, "wb")
        for i in range(len(finalOut)):
            line = str(finalOut[i])
            fout.write(line.encode("utf-8"))
        fout.close()
        '''


        return


def base10ToLetter(number):
    if(number <= 0):
        # invalid
        return ""
    elif(number <= 26):
        return chr(96 + number)
    else:
        #run recursively
        return base10ToBase26Letter(int((number - 1) / 26)) + chr(97 + (number - 1) % 26)

def alphabetToBase10(statement, alphabet):
    number = 0
    for s in statement:
        i = alphabet.find(s)
        if i != -1:
            number *= len(alphabet)
            number += i
    return number

def base10ToAlphabet(number, alphabet):
    result = []
    q = number
    b = len(alphabet)
    k = 0
    while q != 0:
        result.insert(k, q % b)
        # result.append(q % b)
        q = q // b
        k += 1

    statement = ""
    result.reverse()

    for a in result:
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
        return ord(statement) - 96
    else:
        return base26LetterToBase10(statement[1:]) + (26 ** (len(statement) - 1)) * (ord(statement[0]) - 96)

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
        print("not long enough!\n")
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
    sampleRSA.Encrypt("input.txt", "encrypted.txt")
    print("\n")
    #sampleRSA.Decrypt(input("Name of text file: "), "decrypted.txt")
    sampleRSA.Decrypt("encrypted.txt", "decrypted.txt")
    return


if __name__ == "__main__":
    main()
