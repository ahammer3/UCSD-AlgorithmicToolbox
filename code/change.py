# Uses python3
import sys

def get_change(m):
    #write your code here
	count = 0

	count += m // 10
	r1 = m % 10

	count += r1 // 5
	r2 = m % 5

	return count + r2

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
