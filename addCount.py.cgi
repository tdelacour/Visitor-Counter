#!/usr/bin/python
def add():
   f = open("count.txt", "r")
   x = f.read()
   y = int(x.rstrip("/n"))
   z = y+1
   f.close()
   g = open("count.txt", "w")
   g.write(str(z))
   g.close()
print add()
