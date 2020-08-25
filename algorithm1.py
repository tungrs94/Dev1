'''
cho 1 dãy số 123456789
chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100
yêu cầu:
- không dùng package itertools
- không dùng 9 vòng for
'''

n = 9
list_n = [0] * n
nums = '123456789'
total = 100


def att(i):
    for operator in ['+', '-', '']:
        list_n[i] = operator
        if i >= n - 1:
            result = ''
            for j in range(len(nums)):
                result += list_n[j] + nums[j]
            if total == eval(result):
                print(result)
        else:
            att(i + 1)


att(0)
