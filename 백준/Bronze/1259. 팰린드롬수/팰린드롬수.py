while True:
    arr=input("")
    if (arr=='0'):
        break
    else:
        arr2=arr[::-1]
        if(arr==arr2):
            print('yes')
        else:
            print('no')