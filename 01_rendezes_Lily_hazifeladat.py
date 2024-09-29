#!/bin/python3

import math
import os
import random
import re
import sys


def lilysHomework(arr):

    # cserék megszámlálása
    def count_swaps(sorted_arr):
        swaps = 0
        visited = [False] * len(arr)
        index_map = {v: i for i, v in enumerate(arr)}
        
        for i in range(len(arr)):
            if visited[i] or sorted_arr[i] == arr[i]:
                continue

            cycle_size = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = index_map[sorted_arr[x]]
                cycle_size += 1
            
            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps

    # rendezés növekvő és csökkenő sorrendben
    sorted_arr_asc = sorted(arr)
    sorted_arr_desc = sorted(arr, reverse=True)

    # cserék számolása mindkét esetre
    swaps_asc = count_swaps(sorted_arr_asc)
    swaps_desc = count_swaps(sorted_arr_desc)

    # minimum számolás
    return min(swaps_asc, swaps_desc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()