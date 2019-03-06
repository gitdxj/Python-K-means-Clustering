import math


# 仅仅简单地支持二维点集
class Point:
    __m_x = 0
    __m_y = 0

    def __init__(self, coordinate_x, coordinate_y):
        self.__m_x = coordinate_x
        self.__m_y = coordinate_y

    def get_x(self):
        return self.__m_x

    def get_y(self):
        return self.__m_y


# 计算两个点之间的欧式距离
def distance_between_points(a, b):
    a_x = a.get_x()
    a_y = a.get_y()
    b_x = b.get_x()
    b_y = b.get_y()
    dis = (a_x-b_x)*(a_x-b_x) + (a_y-b_y)*(a_y-b_y)
    dis = math.sqrt(dis)
    return dis


# 从csv表格中读入数据
# 其中第一列代表x轴第二列代表y轴
def get_points(filename):
