'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''
'''def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)


if __name__ == "__main__":
	print(compute())'''
def isPalindrome(n):
    s = str(n)
    reverseString = ""
    
    for i in range (len(s) - 1, -1, -1):
        reverseString += s[i]

    return reverseString == s

# returns largest palindrome that is a multiple of two 3 digit numbers
# and returns -1 if no such palindrome exists
def findLargestPalindrome():
    palindrome = -1
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            
            # if product is palindrome and is greater than last recorded palindrome
            if isPalindrome(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;

print (findLargestPalindrome())

