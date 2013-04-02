#!/usr/bin/python
def reader():
    f = open("count.txt", "r")
    x = f.read()
    f.close()
    return x
print reader().rstrip("\n")
