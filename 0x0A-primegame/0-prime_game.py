#!/usr/bin/python3

""" Prime Game """

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0] = is_prime[1] = False
    return [p for p in range(max_num + 1) if is_prime[p]]

def isWinner(x, nums):
    if not nums or x <= 0:
        return None
    
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    # This will store the winner for each game.
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        primes_set = set(p for p in primes if p <= n)
        maria_turn = True
        
        while primes_set:
            prime = min(primes_set)
            primes_set -= set(range(prime, n + 1, prime))
            maria_turn = not maria_turn
        
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
