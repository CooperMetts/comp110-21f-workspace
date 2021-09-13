"""While loop tutoring practice."""

setence: str = input("Write a short sentence: ")
count: int = 0  # number of characters 
i: int = 0
character: str = "a"

while i < len(setence):
    if setence[i] == character: 
        count = count + 1 
    i = i + 1
print(count)
