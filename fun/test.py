'''

1.编写一个函数，接受数字输入，并返回该数字的平方

'''
def pf():
    num = int(input('请输入数字：'))
    return num ** 2

print(pf())

'''
2.编写一个以字符串为参数并将其打印的函数
'''
def print_str(str):
    print(str)

print_str('hello')

'''

4.编写一个带2个函数的程序
第一个函数应接受一个整数为参数，并返回该整数除以2的值
第二个函数应接受一个整数为参数，并返回该整数乘以4的值
调用第一个函数，将结果保存至变量，并将变量作为参数传递给第二个函数

'''


def first(num):
    return num / 2


def second(num):
    return num * 4

num1=14
n=first(num1)

print(second(first(num1)))

'''
5.编写一个字符串转换为float对象并返回该结果的函数，使用异常处理来捕获可能发生的异常
'''
def str_to_float(str):
    try:
        return float(str)
    except:
        print('error')

print(str_to_float('a'))

'''
1.创建一个你喜欢的歌手的列表
2.创建一个由元组构成的列表，每个元组包含居住过或者旅游过的城市的经纬度
3.创建一个包含你的不同属性的字典：身高、最喜欢的颜色、最喜欢的作者
4.编写一个程序，让用户询问你的身高、最喜欢的颜色或者最喜欢的作者，并返回上一个挑战中创建的字典
'''
singer=['zhangxueyou','wangxinlin','liudehua']
city=[('changsha','changde'),('guangzhou','beijing')]
per={'heigh':90,'color':'blue','zhang':'1'}
print(per)


'''
1.打印25到50之间的所有数字
2.打印25到50之间的数字 每个元素及其索引
3.将列表[8,19,148,4]中所有数字与列表[9,1,33,83]中所有的数字相乘，并将结果添加到第3个列表中
4.创建一个名为cubde的模块，在其中写一个模块：接受一个数字作为参数，返回该数字的立方，
并在另外一个模块中导入并调用该函数
'''
num_list = []
for print_num in range(25, 51):
    num_list.append(print_num)
    print(print_num)
print(num_list)
for num in num_list:
    print(num,num_list.index(num))

num1=[8,19,148,4]
num2=[9,1,33,83]
mul=[]
for num3 in num1:
    for num4 in num2:
        mul.append(num3*num4)

print(mul)
'''
创建一个名为cubde的模块，在其中写一个模块：接受一个数字作为参数，返回该数字的立方，
并在另外一个模块中导入并调用该函数
'''

def cubde(num):
    return num ** 3
print(cubde(3))
