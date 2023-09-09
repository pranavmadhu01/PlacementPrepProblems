s = input()
n = len(s)
queue = []
l = []
score = 0
def if_palindrome(string:list)->bool:
    if string == string[::-1]:
        return True
    return False
for i in range(0,n+1):
    if i<n:
        queue.append(i)
        l.append(s[i])
    if if_palindrome(l) and queue[-1]-queue[0]+1 ==4:
        score+=5
    elif if_palindrome(l) and queue[-1]-queue[0]+1 ==5:
        score+=10
        l.pop(0)
        queue.pop(0)
        if if_palindrome(l) and queue[-1]-queue[0]+1 ==4:
            score+=5
    else:
        if queue[-1]-queue[0]+1 ==5:
            l.pop(0)
            queue.pop(0)
print (score)

