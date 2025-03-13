'''
写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间
'''


def hour_to_minu(hour, minu):

    if hour >= 1:
        hourtominu = hour * 60
        return hourtominu+minu
    else:
        return minu
print(hour_to_minu(0,10))