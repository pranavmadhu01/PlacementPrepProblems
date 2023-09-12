string = input()
l = string.split('-')
result = ""
for i in range(len(l)-1,-1,-1):
    if len(l[i])==10 and l[i].isdigit():
        result+=l[i]
        break
if result=="":
    print('No such string exist')
else:
    print(result)

        
