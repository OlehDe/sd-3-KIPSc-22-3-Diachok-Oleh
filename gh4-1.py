def fibonacci_seq_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Приклад використання:
fib_gen = fibonacci_seq_generator()
for _ in range(10):
    print(next(fib_gen))
