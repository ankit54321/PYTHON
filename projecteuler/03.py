'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''
import math
def largest_primeFactor():
    n = 600851475143
    while True:
        p = smallest_primeFactor(n)
        if p < n:
            n //= p
        else:
            return str(n)
def smallest_primeFactor(n):
    assert n>= 2
    for i in range(2,(int)(math.sqrt(n))+1):
        if n % i == 0:
            return i
    return n

if __name__ == "__main__":
    print(largest_primeFactor())
    
