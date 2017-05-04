# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 
n = int(raw_input())
str_arr = []
for x in range(n):
    str_arr.append(raw_input())
baselist = Counter(str_arr)
q = int(raw_input())
for x in range(q): 
    stringlist = raw_input()
    if  stringlist in baselist:
        print baselist[stringlist]
    else:
        print 0