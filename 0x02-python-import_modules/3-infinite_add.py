#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbar = len(sys.argv) - 1
    res = 0
    for i in range(1, nbar + 1):
        res += int(sys.argv[i])
    print(res)
