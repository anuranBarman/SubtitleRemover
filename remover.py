import os
import sys

print("Deleting")
counter = 0  
def getSrts(dirname):
    for x in os.listdir(dirname):
        if os.path.isdir(os.path.join(dirname,x)):
            getSrts(os.path.join(dirname,x))
        else:
            if os.path.splitext(x)[1][1:] == "srt":
                global counter
                counter = counter+1
                os.remove(os.path.join(dirname,x))
                
getSrts(sys.argv[1])
print("Deleted "+str(counter)+" subtitle files.")