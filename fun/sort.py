

num_str=input('请输入一串数字，用逗号隔开：')
num_list1=num_str.split(',')
print(sorted(num_list1, reverse=True))