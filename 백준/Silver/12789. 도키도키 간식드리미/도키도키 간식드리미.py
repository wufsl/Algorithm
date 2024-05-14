
n=int(input())
stack1=[]
order=1
nlist=list(map(int, input().split()))
while (len(nlist)!=0):
    if (order==nlist[0]):
        nlist.pop(0)
        order+=1
        while (len(stack1)!=0 and order==stack1[-1]):
            stack1.pop(-1)
            order+=1   
            
    else:
        stack1.append(nlist[0])
        nlist.pop(0)
        
if (len(stack1)==0):
    print('Nice')
else:
    print('Sad')
        