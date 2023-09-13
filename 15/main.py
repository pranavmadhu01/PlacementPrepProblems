#Ist method
n = input()
l = list(n)
length = len(l)
summ=0
for i in range(0,length):
    summ +=int(l[i])**length
if summ == int(n):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
