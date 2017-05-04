# Enter your code here. Read input from STDIN. Print output to STDOUT
#You are given a list of size , initialized with zeroes. You have to perform  operations on #the list and output the maximum of final values of all the  elements in the list. For every #operation, you are given three integers ,  and  and you have to add value  to all the #elements ranging from index  to (both inclusive).
n, inputs = [int(n) for n in raw_input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in raw_input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
        
        
        
    