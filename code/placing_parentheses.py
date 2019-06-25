# Uses python3
import sys


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

      
def get_maximum_value(dataset):
    #write your code here
    for i in range(len(digits)):
        max_[i][i] = digits[i]
        min_[i][i] = digits[i]
      
    for s in range(len(digits)):
        for i in range(len(digits) - s - 1):
            j = i + s + 1
            min_val, max_val = min_max(i, j)
            max_[i][j] = max_val
            min_[i][j] = min_val
  
  
def min_max(i, j):
    min_val = sys.maxsize
    max_val = -sys.maxsize
    for k in range(i, j):
        a = evalt(max_[i][k], max_[k+1][j], ops[k])
        b = evalt(max_[i][k], min_[k+1][j], ops[k])
        c = evalt(min_[i][k], max_[k+1][j], ops[k])
        d = evalt(min_[i][k], min_[k+1][j], ops[k])
        
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
        
    return min_val, max_val


if __name__ == "__main__":
    dataset = input()
    digits = list(map(int, dataset[0::2]))
    ops = list(dataset[1::2])
    min_ = [[0 for x in range(len(digits))] for y in range(len(digits))]
    max_ = [[0 for x in range(len(digits))] for y in range(len(digits))]
    get_maximum_value(dataset)
    print(max_[0][len(digits) - 1])
