import math
import random

'''
def main():
    runManualTests()

    # 1000000 and 1003000 takes forever, it does work as intended, verified by website http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    runAutomatedTests(1000000, 1003000)

    #print(generatePrimeNumberList(100, 300))


    while True:
        num = int(input("Enter number to be tested if probably prime "))

        if isPrimeMiller(num) == True:
            print("Probably Prime")
        else:
            print("Not Prime")
'''





    # Implement (in Python) a function that takes an integer as input and returns True or False as output,
    #indicating whether or not the integer is prime. Use the Monte Carlo probabalistic algorithm discussed
    #in section 7.2, so that it will finish in reasonable time given several hundred digit test numbers.
    #We will use this piece of code later when we implement RSA encription.

    # Hint: Replace the Python command:
    # remainder = b ** e % n
    # with the equivalent but far faster:
    # remainder = pow(b,e,n)

def isPrimeMiller(n):
    reps = 10
    for i in range(reps):
        ok = millersTest(n)
        if not ok:
            return False
    return True
# for sure not prime
#   return True # n is probably prime

def millersTest(x):

    i = 0
    j = x - 1

    # verifying that we don't have a remainder
    while j / 2 == int:
        i += 1
        j /= 2

    randomVal = random.randrange(2, j)

    # checking remainder
    r = pow(randomVal, j, x)
    if r == 1:
        # valid, always check for remainder == 1
        return True

    for l in range(i+1):
        # j^i % x
        cur = j^l
        # todo, grab the power stuffs
        r = pow(randomVal, cur, x)
        if r == 1:
            return True
    return False

def runManualTests():
    # Prime numbers sourced from http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    primeTests = {
        9619 : None,
        11587 : None,
        13441 : None,
        23197 : None,
        31393 : None,
        37579 : None,
        46181 : None,
        52631 : None,
        54779 : None,
        61333 : None,
    }

    print("Testing Prime numbers. All must pass to proceed.")
    totalPassed = 0

    for key, value in primeTests.items():
        value = isPrimeMiller(key)

        if (value == True):
            totalPassed += 1

        # print out the test results
        print(str(key), "-->", value)
    if totalPassed == 10:
        print("ALL TESTS PASSED\n")
    else:
        print("TESTS FAILED\n")

    # Non prime Tests

    nonPrimeTests = {
        9610 : None,
        11588 : None,
        13442 : None,
        23198 : None,
        31394 : None,
        37570 : None,
        46182 : None,
        52634 : None,
        54770 : None,
        61332 : None,
    }

    print("Testing Non Prime numbers. All must pass to proceed.")
    totalPassed = 0

    for key, value in nonPrimeTests.items():
        value = isPrimeMiller(key)

        if (value == False):
            totalPassed += 1

        # print out the test results
        print(str(key), "-->", value)
    if totalPassed == 10:
        print("ALL TESTS PASSED\n")
    else:
        print("TESTS FAILED\n")

def runAutomatedTests(beg, end):

    primeTests = {}

    primeLst = generatePrimeNumberList(beg, end)

    for item in primeLst:
        primeTests[item] = None

    print("Testing Prime numbers. All must pass to proceed.")
    totalPPassed = 0

    for key, value in primeTests.items():
        value = isPrimeMiller(key)

        if (value == True):
            totalPPassed += 1

        # print out the test results
        print(str(key), "-->", value)
    if totalPPassed == len(primeLst):
        print("ALL TESTS PASSED\n")
    else:
        print("TESTS FAILED\n")

    # NonPrimeTests

    nonPrimeTests = {}

    nonPrimeLst = generateNonPrimeNumberList(beg, end)

    for item in nonPrimeLst:
        nonPrimeTests[item] = None

    print("Testing NonPrime numbers. All must pass to proceed.")
    allPassing = True

    for key, value in nonPrimeTests.items():
        value = isPrimeMiller(key)

        if (value == True):
            allPassing = False

        # print out the test results
        print(str(key), "-->", value)
    if allPassing == True:
        print("ALL TESTS PASSED\n")
    else:
        print("TESTS FAILED\n")


def generatePrimeNumberList(beg, end):
    lst = []
    for i in range(beg, end):
        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False

        if isPrime == True:
            lst.append(i)
    return lst

def generateNonPrimeNumberList(beg, end):
    lst = []
    for i in range(beg, end):
        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                lst.append(i)

    return lst

#if __name__ == "__main__":
#    main()

# Notes from class - 10/1/2021
# IsPrimeMiller(n):
#   reps = 10
#   for i in range(reps):
#       ok = millerstest(n)
#       if not ok:
#            return False # for sure not prime
#   return True # n is probably prime

# Notes from class - 10/4/2021
# refer to pg 286 of the book
# def IsPrimeMiller(n):


# Notes from class - 10/8/2021
# n = 101
# n-1 = 100 = 2^(5)(T) = 2^(2)(25)
# s = 2
# T = 25

# b must be a random number between 2 nad 100
# for now, b = 2
# b^(T) % n is 1    2^(25) % 101 is 1 ? no (10)
# j = 0 b^(2*T) % n is (n-1)    2^(25) % 101 is 100? no
# j = 1     2^50 % 101 is 100? yes

# Notes from class - 10/11/2021
# Refer to pg 463
# Refer to pg 464 example 16
# Monte Carlo algorithm is a chance algorithm
# code example:

# (This is the monteCarlo part of the algorithm)

# def IsPrimeMiller(n):
# for i in range(20):
#   probablyPrime = MillersAlgorithm(N)
#   if not probablyPrime:
#       return False # For sure composite
# return True # almost surely prime

# if n = 11, n-1 = 10 = 2*5, 2'*5, s=1, T = 5
# in this case b is between 2 and 10 inclusive
# b = 10
# b^T % n == 1
# 10^5 % 11


# Another test case
# n = 161
# to find if its prime, try everything up to the square root of it
# n-1 = 160
#       80
#       40
#       20
#       10
#       5
#       s = 5, T = 5
# b is between 2 and 160, 75
# is b^T % n == 1?
# is 75^5 % 161 == 1? (it's 94, so we haven't passed Miller's test yet)
# J tests
# if it passes 0, 1, 2, 3, 4 then it is good enough
# b^((2^J)(T))
# if j = 0, returns 94 No
# if j = 1, returns 142 No
# if j = 2, returns 39 No
# if j = 3, returns 72 No
# if j = 4, returns 32, No
