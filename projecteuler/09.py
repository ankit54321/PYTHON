'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''
def special_PythagoreanTriplet():
    Range = 1000
    for i in range(1,Range + 1):
        for j in range(i+1,Range + 1):
            c = Range-i-j
            if i*i + j*j == c*c:
                print (i,j,c)
                return str(i*j*c)

if __name__ == "__main__":
    print(special_PythagoreanTriplet())
