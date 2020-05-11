#Write a program to input a set of 20 letters. Convert each letter into upper case. Find and display the number of vowels and number of consonants present in the set of given letters.

string = input("Enter a character: ")
upper_string = string.upper()
count_vowel = 0
count_consonants = 0
vowel = set("AEIOU")
for ch in upper_string:
    if ch in vowel:
        count_vowel+= 1
    else:
        count_consonants+= 1
print(f'No. of vowels: {count_vowel} No. of consonants: {count_consonants}')
