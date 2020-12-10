#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbar = len(sys.argv) - 1
    print("{} argument".format(nbar)+((":", "s:")[nbar > 1], "s.")[nbar == 0])
    for i in range(1, nbar + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
