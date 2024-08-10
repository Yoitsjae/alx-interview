#!/usr/bin/python3

""" Prime Game """

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    # Find the maximum number in nums to limit our sieve and DP array
    max_num = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for start in range(2, int(max_num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_num + 1, start):
                is_prime[multiple] = False
    
    # Precompute winners for every number up to max_num
    winner = [0] * (max_num + 1)
    
    for n in range(1, max_num + 1):
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        if not primes:
            winner[n] = 1  # Ben wins if there are no primes
        else:
            for prime in primes:
                if n % prime == 0 and winner[n - prime] == 0:
                    winner[n] = 1
                    break
    
    # Count the wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if winner[n] == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test case
print("Winner: {}".format(isWinner(3, [4, 5, 1])))  # Example from the problem statement
