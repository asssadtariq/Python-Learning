import multiprocessing
import time
import random

is_odd = lambda num: num % 2

def remove_odds(numbers, odd_numbers):
    for num in numbers:
        if is_odd(num):
            odd_numbers.append(num)
            numbers.remove(num)
    

def print_numbers(numbers):
    print(numbers)
    

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        numbers = manager.list([random.randint(0, 10000) for i in range(20)])
        print(f"All Numbers\n",numbers)
        
        odd_numbers = manager.list([])
        
        p1 = multiprocessing.Process(target=remove_odds, args=(numbers, odd_numbers))
        p2 = multiprocessing.Process(target=print_numbers, args=(numbers,))
        p3 = multiprocessing.Process(target=print_numbers, args=(odd_numbers,))
        
        p1.start()
        p1.join()
        
        p2.start()
        p2.join()
        
        p3.start()
        p3.join()
        
        