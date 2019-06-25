# Uses python3
import sys

def optimal_summands(n):
	summands = []
	#write your code here
	k = 1
	v = n
	while True:
		if (v <= (2 * k)):
			summands.append(v)
			break;
		else:
			summands.append(k)
			v -= k
			k += 1

	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
