
'''
1.向Square类添加一个  square_list 类变量，
要求每次创建一个Square对象时，新对象会被自动添加到列表中

2.修改Square类，要求在打印Square对象时候，打印的信息为图形4个边的长度
如假设创建一个Square（29） 则打印 29 by 29 by 29 by 29

3.编写一个函数，接受两个对象作为参数，如果为相同的对象返回True，反则返回False
'''

class Square():
    square_list=[]
    def __init__(self,length,num):
        self.length=length
        self.num=num
        self.square_list.append(self)

    def cacculate_perimeter(self):
        return self.length*4


    def change_size(self):
        self.length=self.length +self.num

    # 重写 __str__ 方法，用于打印实例时的输出
    def __str__(self):
        return f"Square(square_list={self.square_list})"

    # 重写 __repr__ 方法，用于调试时的输出
    def __repr__(self):
        return f"Square(square_list={self.square_list})"


a=Square(1,1)
b=Square(1,1)
print(a.cacculate_perimeter())
print(Square.square_list)