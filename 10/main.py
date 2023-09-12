l = [int(x) for x in input().split()]
#converting to set removes duplicate elements
l = set(l)
count=0
for i in l:
    if i !=0 and i%2==0:
        count+=1
print(len(l)-count)
