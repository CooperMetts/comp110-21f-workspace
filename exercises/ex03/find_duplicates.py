"""Finding duplicate letters in a word."""

__author__ = "730336784"

word: str = input("Give me a word! ")
i: int = 0  # index for how many times the outer loop has run through


while i < len(word): 
    j: int = i + 1
    while j < len(word):
        if word[j] == word[i]:
            print("Found duplicate: True")
            j = len(word)
            i = len(word)
        else: 
            j = j + 1
    i = i + 1
print("Duplicate found: False")
