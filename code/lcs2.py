#Uses python3

import sys


def edit_distance(a, b):
    #write your code here
    res = [[0 for j in range(m+1)] for i in range(n+1)]
    
    longest = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                res[i][j] = res[i-1][j-1] + 1
                if res[i][j] > longest:
                    longest = res[i][j]
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])

    return longest


def lcs2(a, b):
    #write your code here
    return edit_distance(a, b)

  
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
