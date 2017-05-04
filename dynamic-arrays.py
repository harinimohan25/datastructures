# Enter your code here. Read input from STDIN. Print output to STDOUT
n, q = map(int, raw_input().strip().split(' '))
lastAns = 0
empty_list = [[]] * n

for x in range(q):
    qstyle, x, y = map(int,raw_input().strip().split(" "))
    if qstyle == 1:
        index = (x ^ lastAns) % n
        empty_list[index] = empty_list[index] + [y]
    elif qstyle == 2:
        index = (x ^ lastAns) % n
        number = y % len(empty_list[index])
        lastAns = empty_list[index][number]
        print(lastAns)


    
    