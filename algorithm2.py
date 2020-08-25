'''
cho trước 2 số y, x (y > x). Bây h cần tăng x để đạt được giá trị bằng y. Có 2 cách thay đổi giá trị của x:
- tăng gấp đôi x
- bớt x đi 1 đơn vị
Tìm số bước nhỏ nhất để x = y
'''

x = int(input('enter value x:'))
y = int(input('enter value y:'))


def balance(x, y, count=0):
    if y <= x:
        return count + x - y

    if y % 2 != 0:
        y += 1
        count += 1

    y //= 2
    count += 1
    return balance(x=x, y=y, count=count)


print(balance(x, y))
