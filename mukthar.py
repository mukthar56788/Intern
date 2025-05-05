# Sample Python code to print Fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example: Print first 10 Fibonacci numbers
fibonacci(10)
