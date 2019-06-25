# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
   
   
def optimal_sequence_dp(n):
    if n == 1:
        return [1]
   
    operations = min_operations(n)
    return get_min(n, operations)
   
   
def get_min(n, operations):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n -= 1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            if operations[n-1] < operations[n // 2]:
                n -= 1
            else:
                n = n // 2
        elif n % 3 == 0:
            if operations[n-1] < operations[n // 3]:
                n -= 1
            else:
                n = n // 3
              
    return reversed(sequence)
   
   
def min_operations(n):
    res = []
    for i in range(0, n+1):
        res.append(0)
    for i in range(2, n+1):
        min1 = res[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        
        if i % 2 == 0:
            min2 = res[int(i / 2)]
        if i % 3 == 0:
            min3 = res[int(i / 3)]
        
        minimum = min(min1, min2, min3)
        
        res[i] = minimum + 1
        
    return res
   

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
