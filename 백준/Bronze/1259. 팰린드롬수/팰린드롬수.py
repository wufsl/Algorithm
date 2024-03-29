list1=[]
list2=[]
while True:
    arr=input("")
    if (arr=='0'):
        break
    else:
        list1.append(arr)
for j in range(len(list1)):
    for i in list1:
        list2.append(i[::-1])
        
for k in range(len(list1)):
    if(list1[k]==list2[k]):
        print('yes')
    else:
        print('no')
