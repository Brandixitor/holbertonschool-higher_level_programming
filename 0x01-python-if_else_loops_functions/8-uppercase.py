#!/usr/bin/python3
def uppercase(str):
    up = list(str)
    for x in range(len(up)):
        if (ord(up[x]) >= ord('a') and ord(up[x]) <= ord('z')):
            up[x] = chr(ord(up[x]) - 32)
    print("{}".format(("").join(up)))
