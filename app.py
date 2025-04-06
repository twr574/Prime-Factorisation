"""
Prime factorisation calculation via trial division.
"""

import math
import numpy as np
import time

number = int(input("\nInput integer to be factorised. \n"))
factors = list()
root = math.ceil(np.sqrt(number))
c = 2

def findfactor(x,f,rt,l):
    "Test up to the square root, then divide by the factor if found."
    for i in range(l,rt+1):
        if x%i == 0:
            f.append(i)
            findfactor(x/i,f,rt,i)
            return f
    "Return final prime factor if no factors found."
    if x > 1:
        f.append(int(x))
        return f

startTime = time.time()

endlist = findfactor(number,factors,root,c)

endTime = time.time()

"Construct prime factorisation string."
primestr = ""
for i in sorted(set(endlist)):
    if endlist.count(i) > 1:
        primestr = f'{primestr} {i}^{endlist.count(i)} *'
    else:
        primestr = f'{primestr} {i} *'
primestr = primestr[:-2]

print(f'\nPrime factorisation of {number} is: {primestr}. \n\nCalculated in {endTime-startTime} seconds.')
input('\nPress ENTER to close.')
