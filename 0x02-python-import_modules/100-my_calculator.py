#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ar = sys.argv
    nbar = len(ar)
    if nbar != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    res = 0
    op = ar[2]
    a = int(ar[1])
    b = int(ar[3])

    def operation(argument):
        switch = {
            "+": add(a, b),
            "-": sub(a, b),
            "*": mul(a, b),
            "/": div(a, b)
        }
        return (switch.get(argument))
    if ar[2] in ('+', '-', '*', '/'):
        print("{} {} {} = {}".format(a, op, b, operation(op)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
