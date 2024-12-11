#!/usr/bin/python3

""" Prime Game """

def sieve_of_eratosthenes(max_num):
    """ Generate a list of primes up to max_num using the Sieve of Eratosthenes """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for p in range(2, int(max_num ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
    return is_prime

def isWinner(x, nums):
    """ Determine the winner of the prime game after x rounds with different n values """
    if x < 1 or not nums or not all(isinstance(n, int) and n > 0 for n in nums):
        return None

    max_num = max(nums)
    is_prime = sieve_of_eratosthenes(max_num)

    # Precompute cumulative prime counts
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    score = {"Maria": 0, "Ben": 0}
    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if the count is odd
            score["Maria"] += 1
        else:  # Ben wins if the count is even
            score["Ben"] += 1

    # Determine overall winner
    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"
    return None
