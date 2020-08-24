import random
nums = '123456789'
target = 100
para = ['+', '-', '']
total = 0
result = ''
while True:
    for index, num in enumerate(nums):
        if index == len(nums) - 1:
            result += num
        else:
            result += num + random.choice(para)

    if target == eval(result):
        break
    result = ''
print(result)