#!/usr/bin/python3

def isWinner(x, nums):
    def sieve(n):
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (primes[p] == True):
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        primes[0], primes[1] = False, False
        return primes

    def prime_game(n, primes):
        # Initialize available numbers
        available = [i for i in range(1, n + 1)]
        maria_turn = True
        
        while True:
            move_made = False
            for num in available:
                if primes[num]:
                    move_made = True
                    prime = num
                    break

            if not move_made:
                return "Ben" if maria_turn else "Maria"

            # Remove prime and its multiples
            available = [num for num in available if num % prime != 0]

            # Switch turns
            maria_turn = not maria_turn

    # Find maximum number in nums to sieve
    max_n = max(nums)
    primes = sieve(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = prime_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
