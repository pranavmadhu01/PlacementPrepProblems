n = int(input())
first_num = 0
second_num = 1
print(first_num)
print(second_num)
for i in range(2,n):
    third_num = first_num + second_num
    print(third_num)
    first_num = second_num
    second_num = third_num


