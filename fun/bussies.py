'''
5.7 营业税，
随意取一个商品金额，然后根据当地营业税额度计算应该缴纳营业税

5.8计算面积和体积
正方形和立方形
圆和球

'''
import math

def bussise_tax(turnover, tax_rate):
    return turnover * tax_rate


def square_area_volume(length):
    area = length ** 2
    volume = length ** 3
    return area, volume


print('边长为3的正方形的面积是：%d' % square_area_volume(3)[0], '边长为3的正方形体积是：%d' % square_area_volume(3)[1])


def rectangle_are_volume(length, wide, high):
    area = length * wide
    volume = length * wide * high
    return area, volume


print('长方形的面积是：%d' % rectangle_are_volume(3, 4, 5)[0],
      '长方形体积是：%d' % rectangle_are_volume(3, 4, 5)[1])


def circle_are_volume(r, heigh):
    area = math.pi * r ** 2
    volume = math.pi * r ** 2 * heigh
    return area, volume
print('圆的面积是：%d' % circle_are_volume(3,9)[0],
      '圆体积是：%d' % circle_are_volume(3,9)[1])

def sphere_are_volume(r):
    area = 4* math.pi * r ** 2
    volume = 3/4 * math.pi * r ** 23


    return area, volume
print('球的面积是：%d' % sphere_are_volume(3)[0],
      '球体积是：%d' % sphere_are_volume(3)[1])
