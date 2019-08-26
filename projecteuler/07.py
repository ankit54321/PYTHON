'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?'''
import math
def isPrime(n):
    for i in range(2,(int)(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    numOfPrimes = 0
    prime = 1
    while numOfPrimes < n:
        prime += 1
        if(isPrime(prime)):
            numOfPrimes += 1
        
    return prime

print (nth_prime(10001))
