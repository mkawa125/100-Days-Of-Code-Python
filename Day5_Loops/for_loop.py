# Using for loop with the range

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range (1, 101):
    total += number

print(total)

# Sum of even numbers between 1 and 100 OPTION 1
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Sum of even numbers between 1 and 100 OPTION 2
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(f"Summation of even numbers from 1 to 100 is: {total2}")


# FizzBuzz challenge
'''
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''

for number in range(1, 101):
    # % means modular
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)


# PyPython Generator

