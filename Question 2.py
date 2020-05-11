#Write a program to input a character. Display next 5 characters.

ch = input("Enter a character: ")
for i in range (1, 6):
    print(chr(ord(ch) + i))
