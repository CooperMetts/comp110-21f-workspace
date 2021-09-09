"""Repeating a beat in a loop."""

__author__ = "730336784"


# Begin your solution here...

string: str = ""
beat: str = input("What beat do you want to repeat?")
repetitions: int = int(input("How many times do you want to repeat it?"))
x: int = 0

if repetitions <= 0:
    print("No beat...")
else:
    while x < repetitions - 1:
        x: int = x + 1
        string: str = string + beat + " "
    string: str = string + beat
    print(string)
