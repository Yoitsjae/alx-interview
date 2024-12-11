#!/usr/bin/python3

""" Prime Game """

def sieve_of_eratosthenes(max_num):
    """ Generate a list of primes up to max_num using the Sieve of Eratosthenes """
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]

def isWinner(x, nums):
    """ Determine the winner of the prime game after x rounds with different n values """
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1
    
    score = {"Maria": 0, "Ben": 0}

    for n in nums:
        if prime_count[n] % 2 == 1:
            score["Maria"] += 1
        else:
            score["Ben"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"
    
    return None
