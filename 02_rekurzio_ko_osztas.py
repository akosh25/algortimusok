#!/bin/python3

import os

# Rekurzív függvény a kőhalmaz felosztásához
def stoneDivision(n, s):
    # Memoizáció az ismétlődő számítások elkerülésére
    memo = {}

    def dfs(n):
        # Ha már kiszámoltuk ezt a halmazt, akkor az eredményt visszaadjuk
        if n in memo:
            return memo[n]
        
        max_moves = 0
        
        # Iterálunk az összes lehetséges osztón
        for x in s:
            # Csak akkor osztjuk tovább a halmazt, ha az osztható x-szel és az osztás után több, mint 1 részre oszlik
            if n % x == 0 and n != x:
                # Az aktuális mozgás számítása: hányszor tudjuk osztani a részeket és hányszor osztható tovább
                parts = n // x
                max_moves = max(max_moves, parts * dfs(x) + 1)

        memo[n] = max_moves
        return max_moves

    return dfs(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()