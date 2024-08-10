#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for start in range(2, int(max_num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_num + 1, start):
                is_prime[multiple] = False
    
    # Precompute prime counts up to max_num
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    
    # Determine the winner for each number in nums
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test cases
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))  # Expected output: Ben
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected output: Ben
