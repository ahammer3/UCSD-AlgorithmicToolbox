# Uses python3
import sys


def get_change(l, n, m):
    #write your code here
    for cents in range(n+1):
        count = cents
        for j in [c for c in l if c <= cents]:
            if m[cents-j] + 1 < count:
                count = m[cents-j] + 1
        m[cents] = count
        
    return m[n]

   
if __name__ == '__main__':
    n = int(sys.stdin.read())
    l = [1, 3, 4]
    m = [None] * (n+1)
    print(get_change(l, n, m))
