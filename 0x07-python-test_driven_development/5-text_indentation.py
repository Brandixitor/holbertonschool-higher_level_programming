#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    l = (".", "?", ":")
    k = 0
    x = [x for x in text.split(" ") if x.strip()]
    nbwords = len(x)
    for i in range(nbwords):
        wordlen = len(x[i])
        for c in range(wordlen):
            char = x[i][c]
            print(char, end="")
            if char in l:
                k = 1
                print("\n" * 2, end="")
        if i == nbwords - 2:
            if x[i + 1] in l:
                k = 1
        if k == 0 and i != nbwords - 1:
            print(" ", end="")
        k = 0
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
