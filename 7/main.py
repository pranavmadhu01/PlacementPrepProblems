l = [x.upper() for x in input()]
length = len(l)
pointer = length-1
for i in range(length-1,-1,-1):
    pointer = i
    if l[i] not in 'AEIOU':
        print('hello')
        break
string = ""
for i in range(0,length):
    string+=l[i]
else:
    print(string[0:pointer+1])
    