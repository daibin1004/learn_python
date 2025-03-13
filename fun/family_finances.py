'''
 家庭财务
给定一个初始的金额和月开销数，使用循环，确定剩下的金额和当月的支出数，包含最后的支出数
Payment（）函数会用到初始金额和月额度，输出结果应该类似下面的格式
Enter opening balance：100.00
Enter mothly payment:16.13
Amount Remaining
Pymt#      Paid     Balance
-----      ----     ----
0           $0.00   $100
1           $16.13  $83.87
...
7           $3.22   $0.00

'''
balance=100
payment=16.13
print('Pymt#      Paid     Balance')
print('-----      ----     ----')
for mouth in range(1,13):

    if balance>=payment:
        balance=balance-payment
        print(mouth,payment,balance)