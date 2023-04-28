# List is the datatype that can be used to store list of related data piece
# Developers are counting from 0 as an offset from left to tight

states_of_america = ['Mkoko', 'Msata', 'Bagamoyo', 'Dar es salaam']

print(states_of_america)

# Adding item on the list
states_of_america.append('Kibaha')

# Printing the last item in the list
print(states_of_america[-1])

print(states_of_america)

# Treasure map
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])  # 2
vertical = int(position[1])  # 3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
