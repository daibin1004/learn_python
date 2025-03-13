'''
5.17随机数
生成一个有N个元素的由随机数n组成的列表，
其中N和n的取值范围分别为（1<N<=100) 和（0<=n<=2**31 -1)

然后再随机从列表中取 N（1<=N<=100)个随机数出来，
对他们排序，然后显示这个子集

'''
import random

n = 2 ** 31 - 1
N = random.randint(1, 100)
print(n, N)
alist = []
for len in range(1, N):
    alist.append(random.randint(1, n))
    # print(alist)
print(alist)
random_length = random.randint(1, N)
for len1 in range(random_length):
    print(alist[len1])

