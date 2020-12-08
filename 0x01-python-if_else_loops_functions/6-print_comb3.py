#!/usr/bin/python3
for x in range(0, 9):
    for w in range(x + 1, 10):
        print("{}{}".format(x, w), end="")
        print((", ", "\n")[x == 8 and w == 9], end="")
