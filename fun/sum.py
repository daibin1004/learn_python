


# 写一个函数，计算并返回两个数的乘积
# 写一段代码调用函数，显示结果
def num_product(num1, num2):
    return num1 * num2


print(num_product(3, 2))


'''
3.输入一个测试成绩，根据下面的标准，输出她的评分成绩A-F
A：90-100
B：80-89
C：70-79
D：60-69
F：<60
'''
try:
    score = int(input('请输入你的分数'))
    if score >= 90 and score <= 100:
        print('A')
    elif score >= 80 and score <= 89:
        print('B')
    elif score >= 70 and score <= 79:
        print('C')
    elif score >= 60 and score <= 69:
        print('D')
    else:
        print('F')
except:
    print('error')



'''
4.判定给定的年份是否闰年
公式：
一个闰年就是她可以被4整除，但不能被100整除，或者既可以被400整除

1992  1996  2000 闰年
1967  1900 不是
下一个是2400
'''
def is_leap_year(year):
    # 判断是否为闰年
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

# 测试
year = 2400
if is_leap_year(year):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

