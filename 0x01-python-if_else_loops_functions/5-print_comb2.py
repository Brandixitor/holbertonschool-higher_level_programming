#!/usr/bin/python3
for x in range(0, 100):
    print("{:02d}".format(x), end="")
    print(("\n", ", ")[x != 99], end="")
