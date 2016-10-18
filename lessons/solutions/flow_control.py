# Intro to while loops:
# A simple example:
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
    print('Blastoff!')

# lesson 3 Bonus:
from string import ascii_lowercase
word = ''
total = 0
for char in word:
    letter_value = 1
    for letter in ascii_lowercase:
        if letter == char:
            total += letter_value
            break
        letter_value += 1
print(total)
