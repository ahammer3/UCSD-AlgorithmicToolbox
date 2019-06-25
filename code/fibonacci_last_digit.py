# Uses python3
import sys

def fibonacci_last_digit(n):
 
    nums = [None] * (n+2)
    nums[0] = 0
    nums[1] = 1
    
    for i in range(2, n+1):
        nums[i] = (nums[i-1] + nums[i-2]) % 10

    return nums[n]

if __name__ == '__main__':
 	# for stdin, end input with newline and CRTL + D
	input = sys.stdin.read()
	n = int(input)
	print(fibonacci_last_digit(n))
