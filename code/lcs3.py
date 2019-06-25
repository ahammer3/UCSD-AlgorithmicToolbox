#Uses python3

import sys


def edit_distance(a, b, c):
    # the lcs2 program builds very well up to this one - almost trivial
    res = [[[0 for k in range(cn+1)] for j in range(bn+1)] for i in range(an+1)]
    
    longest = 0
    
    for i in range(1, an+1):
        for j in range(1, bn+1):
            for k in range(1, cn+1):
                if a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    res[i][j][k] = res[i-1][j-1][k-1] + 1
                    if res[i][j][k] > longest:
                        longest = res[i][j][k]
                else:
                    res[i][j][k] = max(res[i-1][j][k], res[i][j-1][k], res[i][j][k-1], res[i][j-1][k-1], res[i-1][j-1][k], res[i-1][j][k-1])

    return longest


def lcs3(a, b, c):
    #write your code here
    return edit_distance(a, b, c)

  
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
