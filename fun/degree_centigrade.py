'''
写一对函数对华氏度 到摄氏度转换
C=(F-32)*(5/9)使用真正的除法
'''

def fahrenheit_to_degress(f_num):
    return (f_num-32)*(5/9)

print('转换后的摄氏度是：%f' % fahrenheit_to_degress(100))