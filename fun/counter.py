'''

5-6.写一个计算机程序
你的代码可以接受这样的表达式，两个操作数加一个操作符：N1 操作符 N2
其中 N1和N2为整型或者浮点型，操作符可以是+ - * / % ** 分别表示 加减乘整除  取余  幂运算
计算这个表达的结果，然后显示出来
可以使用字符串split()，不可使用eval()
'''
def counter1(sting_num):
    num_list=sting_num.split()
    try:

         N1=int(num_list[0])
         operator=num_list[1]
         N2=int(num_list[2])
    except ValueError:
        try:
             N1 = float(num_list[0])
             operator = num_list[1]
             N2 = float(num_list[2])
        except ValueError:
            print('error')

    # 定义运算符映射
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        '//': lambda x, y: x // y if y != 0 else "Error: Division by zero",
        '%': lambda x, y: x % y if y != 0 else "Error: Division by zero",
        '**': lambda x, y: x ** y
    }

    # 检查运算符是否有效
    if operator in operations:
        return operations[operator](N1, N2)
    else:
        print(f"Error: Unknown operator '{operator}'")
        return None
print(counter1('7 + 19'))
