x = 10
y = 20
count = 0
while True:
    if x < y:
        x = x * 2
    elif x > y:
        x = x - 1

    count += 1
    if x == y:
        break
print(count)