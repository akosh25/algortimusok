def next_palindrome(k):
    k = list(k)
    n = len(k)

    if k == k[::-1]:  
        k = list(str(int(''.join(k)) + 1))
        n = len(k)

    half_len = (n + 1) // 2
    left_half = k[:half_len]
    if n % 2 == 0:
        palindrome = left_half + left_half[::-1]
    else:
        palindrome = left_half + left_half[-2::-1]

    if ''.join(palindrome) > ''.join(k):
        return ''.join(palindrome)

    left_half = list(str(int(''.join(left_half)) + 1))
    if n % 2 == 0:
        palindrome = left_half + left_half[::-1]
    else:
        palindrome = left_half + left_half[-2::-1]

    return ''.join(palindrome)

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        k = input().strip()
        results.append(next_palindrome(k))

    print("\n".join(results))

if __name__ == "__main__":
    main()