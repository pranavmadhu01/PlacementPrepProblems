n = int(input())
l = [int(input()) for x in range(n)]
for i in range(0,n):
    if l[i]<0:
        l[i] = l[i]*l[i]
print(l)