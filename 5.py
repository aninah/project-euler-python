from math import *

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def factor(x):
    factors = []
    store = x
    while store > 1:
        if isPrime(store):
            factors.append(store)
            store = 0
        elif not isPrime(store):
            for i in range(2,x):
                if store%i == 0 and isPrime(i) and not(i == 1):    
                        factors.append(i)
                        store /= i
        if store == 1:
            store = 0
    factors.sort()
    return factors
def almost(num):
    look_up = {}
    final = 1
    for f in range(2,num+1):
        if isPrime(f):
            look_up[f] = 0
    for i in range(2,num+1):
        #loop through num
        arr = factor(i)
        #factor i, return factor array
        for l in arr:
            #loop thru factor array
            store = arr.count(l)
            if look_up[l] <= store:
                look_up[l] = store
    primekeys = look_up.keys()
    for j in primekeys:
        temp = look_up[j]
        t = j**temp
        final *= t
    return final
    
print almost(20)

#completed August 2015
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

