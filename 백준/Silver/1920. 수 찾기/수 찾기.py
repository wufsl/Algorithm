import sys
n=int(sys.stdin.readline())
nset=set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
mlist=list(map(int,sys.stdin.readline().split()))

for i in mlist:
    if i in nset:
        print(1)
    else:
        print(0)
            