#Write a program  to generate all the alternate letters in the range of letters from A to Z.

ch = input("Enter the first character of alphabet: ")
for i in range (0,25, 2):
    print(chr(ord(ch) + i))
