#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format((chr(i), chr(i - 32))[i % 2]), end="")
