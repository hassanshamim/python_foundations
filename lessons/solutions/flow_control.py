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


# Leap year options:
# Option 1
year = 1909
if year % 4 == 0:
    if year % 400 == 0:
        print('Leap')
    elif year % 100 == 0:
        print('Normal')
    else:
        print('Leap')
else:
    print('Normal')

# Option 2
year = 5
if year % 400 == 0:
    print('Leap')
elif year % 100 == 0:
    print('Normal')
elif year % 4 == 0:
    print('Leap')
else:
    print('Normal')
