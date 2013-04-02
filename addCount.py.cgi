#!/usr/bin/python
def add():
   f = open("count.txt", "r")
   x = f.read()
   y = int(x[0:1])
   z = y+1
   f.close()
   g = open("count.txt", "w")
   g.write(str(z))
print add()
