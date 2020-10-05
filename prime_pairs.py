def Sieve_of_Eratosthenes(n):
    """Create list of primes up to n"""
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def bruteforce_solutions(remaining, result):
    """Sort list of numbers (remaining),
    so every pair added together results in a prime.
    Recursive.
    """

    # no ints left in remaining = success
    if len(remaining) == 0:
        return(result)

    # first call
    if len(result) == 0:
        results = []
        for i, num in enumerate(remaining):
            temp = bruteforce_solutions(remaining[:i] + remaining[i + 1:], [num])
            if temp:
                results.append(temp)
        return results
    # self calls
    else:
        for i, num in enumerate(remaining):
            if ((result[-1] + num) in primes):
                temp = bruteforce_solutions(remaining[:i] + remaining[i + 1:], result + [num])
                if temp:
                    return temp


nums = [i for i in range(1, 10)]  # remember: range is include to exclude
primes = Sieve_of_Eratosthenes(nums[-1] * 2)
all_solutions = bruteforce_solutions(nums, [])
for i, solution in enumerate(all_solutions):
    print(f"Solution {i}: {solution}")