#!/usr/bin/python
import sys
import re
f = open("osName.txt", "r")
g = open("osCount.txt", "r")
osName = re.split(',',f.read().rstrip("\n"))
osCount = re.split(',',g.read().rstrip("\n"))
f.close()
g.close()
def listChecker(arg):
   arg1 = arg.replace("\\","")
   if arg1 in osName:
     x = osName.index(arg1)
     osCount[x] = str(int(osCount[x])+1)
     text = osCount[0]
     for ele in osCount[1:len(osCount)]:
        text = text + "," + ele
     a = open("osCount.txt", "w")
     a.write(text)
     a.close()
   else: 
     osName.append(arg1)
     text1 = osName[0]
     for ele in osName[1:len(osName)]:
        text1 = text1 + "," + ele
     b = open("osName.txt", "w")
     b.write(text1)
     b.close()
     osCount.append(1)
     text2 = str(osCount[0])
     for ele in osCount[1:len(osCount)]:
        text2 = text2 + "," + str(ele)
     c = open("osCount.txt", "w")
     c.write(text2)
     c.close()
   for ele in osName:
     if ele != "":
       x = osName.index(ele)
       print ele , "----------------------------------->" , str(osCount[x]) + "*"
listChecker(sys.argv[1])
