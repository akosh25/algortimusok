#!/bin/python3

import math
import os
import random
import re
import sys

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        # Ha a konyvtar epitesi koltsege olcsobb vagy egyenlo, mint az ut koltsege,
        # akkor minden varosban kulon konyvtar epitese a legolcsobb megoldas.
        return n * c_lib

    # Szomszedsagi lista letrehozasa a varosok kozotti kapcsolatok tarolasara
    adj_list = [[] for _ in range(n + 1)]
    for city1, city2 in cities:
        adj_list[city1].append(city2)
        adj_list[city2].append(city1)

    # Latogatott varosok nyilvantartasa, hogy nyomon kovessuk, 
    # melyik varosokat jartuk mar be
    visited = [False] * (n + 1)
    
    def dfs(city):
        # Melysegi kereses (DFS) hasznalata egy komponens bejarasara
        stack = [city]
        size = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                # Megjeloljuk, hogy a varost mar meglatogattuk
                visited[node] = True
                size += 1
                for neighbor in adj_list[node]:
                    # Csak a nem latogatott szomszedokat adjuk hozza a bejarasi listahoz
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return size

    # Osszkoltseg kiszamitasa
    total_cost = 0
    for city in range(1, n + 1):
        if not visited[city]:
            # Ha a varost meg nem latogattuk meg, uj komponenshez tartozik
            component_size = dfs(city)
            # Minden komponenshez hozzaadjuk egy konyvtar epitesi koltseget 
            # valamint a kapcsolodo varosokat osszekoto utak koltseget
            total_cost += c_lib + (component_size - 1) * c_road

    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()