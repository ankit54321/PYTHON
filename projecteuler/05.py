'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 


def smallestMultiple():
    ans = 1
    for i in range(1,21):
        ans *= i // gcd(1,ans)
    return str(ans)

if __name__ == "__main__":
    print(smallestMultiple())
