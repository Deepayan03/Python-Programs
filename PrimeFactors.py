def primeFactors(n):
    factors = []  # List to store prime factors
    
    # Check for 2 as a factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    i = 3
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2
    
    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        factors.append(n)
    return factors;


print(primeFactors(85))

