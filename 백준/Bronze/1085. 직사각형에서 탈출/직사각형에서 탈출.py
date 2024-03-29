x,y,w,h=map(int, input().split())
x_value=0
y_value=0

if((w-x)>x):
    x_value = x
else:
    x_value = w-x

if ((h-y)>y):
    y_value = y
else:
    y_value = h-y

if(x_value>y_value):
    print(y_value)
else:
    print(x_value)