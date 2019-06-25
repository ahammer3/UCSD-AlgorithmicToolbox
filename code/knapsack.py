# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    res = [[0 for x in range(W+1)] for y in range(n+1)]
   
    for i in range(1, n+1):
        for weight in range(1, W+1):
            if i == 0 or weight == 0:
                res[i][weight] = 0
            elif w[i-1] <= weight:
                res[i][weight] = max(w[i-1] + res[i-1][weight - w[i-1]], res[i-1][weight])
            else:
                res[i][weight] = res[i-1][weight]
              
    return res[n][W]
   
   
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
