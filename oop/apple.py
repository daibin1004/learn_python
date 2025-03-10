'''
1.定义一个Apple类，创建4个实例变量，表示苹果的4种属性
'''

class Apple():
    def __init__(self,color,height,weight,good_bad):
        self.color=color
        self.height=height
        self.weight=weight
        self.good_bad=good_bad

zhang=Apple('red',1,13,'good')
print(zhang.good_bad)
'''
2.定义一个Circle类，创建area 方法计算面积。
然后创建一个Circle对象，调用area方法，打印结果
可使用Python内置的math模块的pi函数
'''
class Circle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

zhang=Circle(1,10)
print(zhang.area())

'''
3.定义一个  Triangle    类，创建area方法计算并返回面积，创建一个TRiangle对象，调用area方法，打印结果
'''
class Triangle():

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length* self.width

triangle=Triangle(2,8)
print(triangle.area())

'''
4.定义一个  Hexagon 类，创建    cacculate_perimeter 方法，计算并返回周长
然后创建一个Hexagon对象，调用calculate_perimter方法，并打印结果
'''
class Hexagon():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def cacculate_perimeter(self):
        return (self.length+self.width)*2

hex=Hexagon(3,19)
print(hex.cacculate_perimeter())


'''
