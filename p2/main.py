def cnt_3(num) :
    count = 0
    if num == 0 :
        return 0
    elif num % 10 == 3 :
        return 1 + cnt_3(num // 10)
    else :
        return cnt_3(num // 10)

def total(num) :
    if num == 0 :
        return 0
    else :
        return cnt_3(num) + total(num - 1)

num = int(input())
print(total(num))
