import os
from os import path
import sys
season={1:"Wnt", 2:"Wnt",3:"Wnt", 4:"Spr", 5:"Spr", 6:"Spr", \
        7:"Sum", 8:"Sum",9:"Sum", 10:"Aut", 11:"Aut", 12:"Aut"}
nalerts=0
nerrors=0
filename=input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file=open(filename,"r")

while 1:
    line=file.readline()
    if line=="":
        break                          # Break causes the while loop to end

    ## Add lines from lecture notes here
    
    if line.find("Temperature:") >= 0:  # This is a Temperature data line
        T_list=line.split()
        date=T_list[0].split("/")
        for i in range(3):
            date[i]=int(date[i])
        T_value=float(T_list[2])
        print("Year=%4d Month=%02d Day=%02d Season=%3s  T=%4.1f"\
            %(date[2],date[1],date[0],season[date[1]],T_value))

    ## Add lines from lecture notes here
    if line.find("Error") >= 0:  # This is an error line
        nerrors+=1
print("Total alerts=%d, Total errors=%d"%(nalerts, nerrors))
