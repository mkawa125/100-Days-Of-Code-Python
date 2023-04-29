
# For loop
"""
for item inlist_of_items
    #Do something to each list

for number in range (a, b)
    #Print (number)
"""

# While loop
"""
number = 0
while number > 0:
    Do something to each list
    number -= 1
    print(number)
"""

number = 8
while number > 0:
    print(f"This is the step number: {number}")
    number -= 1


# Escaping the maze
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""