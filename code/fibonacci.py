# Uses python3
def calc_fib(n):

    nums = [None] * (n+2)
    nums[0] = 0
    nums[1] = 1
    
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]

    return nums[n]

n = int(input())
print(calc_fib(n))
