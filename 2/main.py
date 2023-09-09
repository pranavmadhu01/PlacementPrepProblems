import math
n = int(input())
# l = [int(x) for x in input().split()]
l = [int(input()) for x in range (n)]
count = 0
for i in l:
    temp = math.sqrt(i)
    if temp == int (temp):
        count  = count+1
print(count)




