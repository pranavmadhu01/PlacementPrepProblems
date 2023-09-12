n = int(input())
l = [int(x) for x in input().split()]
b = []
for i in range(1,n):
    b.append(abs(l[i]-l[i-1]))
s  = 0
for i in range(0,len(b)):
    s += (b[i]^i)
print(s%(10**9+7))