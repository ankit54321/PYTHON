#Write a program  to input a character. Find and display the next 10th character in the ASCII table.

ch = input("Enter the first character: ")
ch_1 = ord(ch) + 10
print(f'The next 10th character is : {chr(ch_1)}')

