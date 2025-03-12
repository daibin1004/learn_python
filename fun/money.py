'''
5.取一个任意小余1美元的金额，然后计算可以换成最少多少个硬币
硬币为1美分、5美分、10美分，25美分  4种
1美元=100美分
例子：0.76美元换算结果是3个25美分，1个1美分

'''
def min_coins(num):
    s_fen=int(num*100)
    conis=[25,10,5,1]
    result={}
    for  coni in conis:
        count=s_fen//coni
        result[coni]=count
        s_fen-=count*coni

    return result
print(min_coins(0.76))