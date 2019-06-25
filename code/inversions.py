# Uses python3
import sys

def get_number_of_inversions(A):
    [count, sorted_] = merge_sort(A)
  
    return count

  
def merge_sort(A):
    if len(A) <= 1:
        return [0, A]
    else:
        mid = len(A) // 2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        
        return merge(left, right)
       
       
def merge(B,C):
    count = B[0] + C[0]
    left = B[1]
    right = C[1]
    
    res = []
 
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(left[0])
            count += len(right)
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
            
    res += left
    res += right
      
    return [count, res]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a))
