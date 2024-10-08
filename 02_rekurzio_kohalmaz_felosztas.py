#!/bin/python3

import os

# Rekurziv fuggveny a kohalmaz felosztasahoz
def stoneDivision(n, s):
    
    # az ismetlodo szamitasok elkerulesere
    memo = {}

    def dfs(n):
        # ha mar kiszamoltuk ezt a halmazt, akkor az eredmenyt visszaadjuk
        if n in memo:
            return memo[n]
        
        max_moves = 0
        
        # iteralunk az osszes lehetseges oszton
        for x in s:
            # csak akkor osztjuk tovabb a halmazt, ha az oszthato x-szel és az osztas utan tobb, mint 1 reszre oszlik
            if n % x == 0 and n != x:
                # az aktualis mozgas szamitasa: hanyszor tudjuk osztani a reszeket és hanyszor oszthato tovabb
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