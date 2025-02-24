import time

def prime_generator():
    num = 2
    while True:
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            yield num
        num += 1

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time taken: {execution_time:.30f} seconds")
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    prime_gen = prime_generator()
    return [next(prime_gen) for _ in range(n)]

prime_numbers = prime_num_getter(100)
print(prime_numbers)
