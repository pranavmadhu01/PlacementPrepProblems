#Ist approach
n = input()
n = n[::-1]
print(int(n))
#IInd approach
n = int(input())
n = str(n)[::-1]
print(int(n))
#IIIrd approach
n  = int(input())
rev = 0
while n!=0:
    rev = (rev*10) + (n%10)
    n = n//10
print(rev)
 