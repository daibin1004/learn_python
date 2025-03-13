'''
 最大公约数和最小公倍数，请计算2个整型的最大公约数和最小公倍数
最大公约数是能够同时整除两个数的最大正整数。
最小公倍数是能够同时被两个数整除的最小正整数。

'''
import math


def common_num(num1,num2):
    return math.gcd(num1,num2),math.lcm(num1,num2)

print(common_num(3,6))