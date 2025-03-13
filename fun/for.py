'''
使用循环和算术运算，求出0-20之间的所有偶数和奇数
辨别奇数和偶数的最简单方式是什么
写函数，检测一个整数能否被另外一个整数整除；用户输入2个整数，然后 函数判断2个数是否有整除关系，返回True和False

divisibility
'''
odd = []
even = []
for num in range(0, 21):
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


def divisibility(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


print(divisibility(6, 3))
