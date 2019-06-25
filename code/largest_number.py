#Uses python3

import sys
import math

def greater(digit, max_digit):
	return digit + max_digit > max_digit + digit

def largest_number(a):
	#write your code here
	res = ""
	while len(a) != 0:
		max_digit = '0'
		for ai in a:
			if greater(ai, max_digit):
				max_digit = ai
		res += max_digit
		a.remove(max_digit)
	return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    