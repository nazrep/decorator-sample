import random
import time

def my_decorator(fn):
    def wrapper():
        current_time = time.time()
        fn()
        print('it took', time.time() - current_time, 'seconds')
    return wrapper

@my_decorator
def generate_random_nums():
    numbers = [i for i in range(0, 100000)]
    random.shuffle(numbers)
    print(numbers)

generate_random_nums()

