n = int(input())
l = [int(x) for x in input().split()]
for i in range(0,n):
    l[i] = l[i]>>2
summ = sum(l)
if summ>(10**9+7):
    summ = summ%(10**9+7)
print(summ)