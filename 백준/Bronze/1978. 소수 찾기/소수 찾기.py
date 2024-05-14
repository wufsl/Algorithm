num=int(input())
nums=list(map(int,input().split()))
cnt=0
for i in range(len(nums)):
    is_prime=True
    if nums[i] <2:
        is_prime=False
    for j in range(2,nums[i]):
        if nums[i] % j==0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)
    