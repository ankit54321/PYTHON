#Write a program in Java to accept an integer number N such that 0<N<27. Display the corresponding letter of the alphabet (i.e. the letter at position N).
#[Hint: If N =1 then display A]

n = (int)(input('Enter an integer: '))
if n>0 and n<27:
    ch = chr(n + 64)
else:
    print('Please enter a number between 0 and 27')

print(f'The corresponding letter of the alphabet: {ch}')

