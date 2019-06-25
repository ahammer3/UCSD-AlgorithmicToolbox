# Uses python3
import sys

def fibmod(n, m):
    assert 1 <= n <= 10**18, n
    assert 2 <= m <= 10**5, m

    def f(n):
        if n == 0:
            return 0, 1
        else:
            a, b = f(n // 2)
            c = a * (2*b - a) % m
            d = (a**2 + b**2) % m

            if n % 2 == 0:
                return c, d
            else:
                return d, (c + d) % m

    return f(n)[0]
   
def fib_partial_sum(n, m):
 
	return (fibmod(m+2, 10) + 10 - fibmod(n+1, 10)) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_partial_sum(from_, to))