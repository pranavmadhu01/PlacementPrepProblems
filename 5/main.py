n = int(input())
l = [int(x) for x in input().split()]
l.sort()
small_prime = -1
large_prime = -1
def if_Prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
for i in range(0,n):
    if l[i]<=0 or l[i]==1 :
        continue
    if if_Prime(l[i]):
        if small_prime==-1:
            small_prime = l[i]
        else:
            large_prime = l[i]
print(abs(small_prime-large_prime))




