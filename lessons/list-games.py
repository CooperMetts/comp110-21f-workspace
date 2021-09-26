"""Examples of using lists in a sample 'game'."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)  # if you don't give it a parameter, it  will remove the last item of the list by default.
print(rolls) 

# Sum  the values of our rolls:
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}.")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item 
# print(rolls[0])  # This accesses the value of rolls at index 0.
# print(rolls[1])  # This accesses the value of rolls at index 1.

# # Accessing length of list
# print(len(rolls))

# # Acessing last item of a list
# print(rolls[len(rolls)] - 1)

# # or 

# last_index: int = len(rolls) - 1
