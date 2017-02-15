import argparse
import os
import re
import sys

def is_not_int(x):
    try:
        x = int(x)
        return False
    except:
        return True

parser = argparse.ArgumentParser(description='look for files that start with sim')
parser.add_argument('filepath', type=str, nargs=1)
args = parser.parse_args()
mypath = args.filepath[0]
# print(mypath)
onlyfiles = [d for d in os.listdir(mypath) if os.path.isdir(os.path.join(mypath,d))]
# print(onlyfiles)
pattern = re.compile('^sim')
onlyfiles = filter(pattern.match, onlyfiles)
for i in range(len(onlyfiles)):
    print("%d %s" % (i, onlyfiles[i]))
print("Type in the number?")
j = sys.stdin.readline()
if is_not_int(j):
    j = -1
else:
    j = int(j)
while j < 0 or j > len(onlyfiles):
    print("Type in the number?")
    j = sys.stdin.readline()
    if is_not_int(j):
        j = -1
    else:
        j = int(j)
print(re.sub("^sim",'',onlyfiles[j]))