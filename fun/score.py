'''
5-3.
标准类型操作符。写一段脚本,输入一个测验成绩,根据下面的标准,输出他的评分成绩(A-F)。
A:90~100
B:80~89
C:70~79
D:60~69
F:<60

6-4.算术。更新上一章里面你的得分测试练习方案，把测试得分放到一个列表中去。你的代码应该
可以计算出一个平均分，见练习2-9和练习5-3。
'''

score_str=input('请输入测试成绩,使用,分隔：')
score_lst=score_str.split(',')

score_sum=0
for score in score_lst:
    score=int(score)
    score_sum+=score
    if score >= 90 and score <= 100:
        print('A')
    elif score >= 80 and score <= 89:
        print('B')
    elif score >= 70 and score <= 79:
        print('C')
    elif score >= 60 and score <= 69:
        print('D')
    elif score < 60 and score >= 0:
        print('F')
    else:
        print('Error')
print(score_sum/len(score_lst))
