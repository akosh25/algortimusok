#!/bin/python3

import math
import os
import random
import re
import sys


def stockmax(prices):
    max_price = 0
    profit = 0
    
    # az árlista bejárása visszafelé!
    for price in reversed(prices):
        #  ha az aktuális ár magasabb - frissítjük a max. árat
        if price > max_price:
            max_price = price
        # nyereség: max ár - aktuális ár 
        profit += max(0, max_price - price)
    
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
