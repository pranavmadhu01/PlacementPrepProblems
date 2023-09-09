n = int(input())
l = [int(x) for x in input().split()]
A_couple = 0
B_couple = 0
for i in range(1,n):
    area = l[i]*l[i-1]
    perimeter = 2*(l[i]+l[i-1])
    if area>perimeter:
        A_couple+=1
    else:
        B_couple+=1
print(abs(A_couple - B_couple))
