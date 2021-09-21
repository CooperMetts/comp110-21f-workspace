"""An exercise in remainders and boolean logic."""

__author__ = "730336784"


# Begin your solution here...

number: int = int(input("Give me a number! "))

if number % 2 == 0 + number % 7 == 0: 
    print("TAR HEELS")
else:
    if number % 7 == 0: 
        print("HEELS")
    else: 
        if number % 2 == 0: 
            print("TAR")
        else:
            print("CAROLINA")
