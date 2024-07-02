import multiprocessing
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

def main():
    num_processes = multiprocessing.cpu_count()
    range_start = 2
    range_end = 1000000
    chunk_size = (range_end - range_start) // num_processes

    processes = []
    results = multiprocessing.Manager().list()

    for i in range(num_processes):
        start = range_start + i * chunk_size
        end = start + chunk_size
        if i == num_processes - 1:  # last process takes care of the rest
            end = range_end + 1
        p = multiprocessing.Process(target=lambda r, s, e: r.append(find_twin_primes(s, e)), args=(results, start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    all_twin_primes = []
    for result in results:
        all_twin_primes.extend(result)

    print("Found twin prime pairs:")
    for pair in all_twin_primes:
        print(pair)

if __name__ == "__main__":
    main()
