n=int(input())
time = list(map(int, input().split()))
time.sort()
total=0
current=0
for i in time:
    current+=i
    total+=current

print(total)