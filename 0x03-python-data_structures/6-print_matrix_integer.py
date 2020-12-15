#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for b in range(len(matrix[i])):
            print("{:d}".format(matrix[i][b]), end="")
            if (b != len(matrix[i]) - 1):
                print(" ", end="")
        print("")
