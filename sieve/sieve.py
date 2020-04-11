from typing import List


def sieve_in_interval(lower_bound: int, upper_bound: int) -> List[int]:
    if lower_bound < 2 or lower_bound > upper_bound:
        raise ValueError("Lower bound must be at least 2 " +
                         "and bigger or equal as upper bound")

    primes = [i for i in range(upper_bound + 1)]
    current = 2

    # Overwrite all multiplies by 0
    while current * current <= upper_bound:
        if primes[current] != 0:
            for i in range(current * current, upper_bound + 1, current):
                primes[i] = 0
        current += 1

    # All non zero numbers are primes
    return list(filter(lambda number: number != 0 and number >= lower_bound, primes))


def calculate_primes_in_interval() -> None:
    lower_bound = int(input("Enter lower bound: "))
    upper_bound = int(input("Enter upper bound: "))
    print(sieve_in_interval(lower_bound, upper_bound))
