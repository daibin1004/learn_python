'''
元组中的列表 这类可变元素支持修改的
'''
t=(['a',1],'who')
print(t,id(t))
t[0][0]=9
print(t,id(t))
