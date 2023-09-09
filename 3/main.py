import math
n = int(input())
l = [int(x) for x in input().split()]
s = set()
for i in range (1,n):
    g = math.gcd(l[i-1],l[i])
    lcm = (l[i-1]*l[i])//g
    s.add(lcm)
print(min(s))