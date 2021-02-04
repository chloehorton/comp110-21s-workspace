"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
integer: int = int(input("Pick an integer:"))
if integer%2 == 0 and integer%7 == 0:
    print("TAR HEELS")
else:
    if integer%7 == 0:
        print("HEELS")
    else:
        if integer%2 == 0:
            print("TAR")
        else:
            print("CAROLINA")