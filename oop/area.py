'''
 1.创建    Rectangle   和  Square   类，使他们均有一个canculate_perimeter的方法，
计算所表示的图形的周长
创建Rectangle和sqaure对象，并调用二者的周长计算方法
'''


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cacculate_perimeter(self):
        return (self.width + self.length) * 2


class Square():
    def __init__(self,length):
        self.length=length

    def cacculate_perimeter(self):
        return self.length*4

a=Rectangle(3,5)
b=Square(4)
print(a.cacculate_perimeter(),b.cacculate_perimeter())

'''
2.在Square类中，定义一个叫change_size的方法，支持传入一个数字，增加或者减少Square对象的周长
'''
class Square():
    def __init__(self,length,num):
        self.length=length
        self.num=num

    def cacculate_perimeter(self):
        return self.length*4

    def change_size(self):
        self.length=self.length +self.num

a=Square(4,1)
a.change_size()
print(a.cacculate_perimeter())

'''
3.创建一个  Shape   类，在其中定义一个叫  what_am_i   的方法，被调用时候打印'I am s shape'
调整上个挑战中的Square和Rectangle类，使其继承  Shape   类，然后创建Sqaure和Rectangle对象，
并在二者上调用新方法
4.创建一个Horse类，以及一个叫Rider类，使用组合，表示一批有骑手的马
'''
class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print('I am s shape')

class Square(Shape):
    def __init__(self,length,num):
        self.length=length
        self.num=num

    def cacculate_perimeter(self):
        return self.length*4

    def change_size(self):
        self.length=self.length +self.num
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cacculate_perimeter(self):
        return (self.width + self.length) * 2

s=Square(3,1)
r=Rectangle(1,2)
print(s.cacculate_perimeter())
print(r.cacculate_perimeter())
print(s.what_am_i())
print(r.what_am_i())

