import math
import csv
import matplotlib.pyplot as plt


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

    def prn(self):
        print("(" + str(self.__m_x) + ", " + str(self.__m_y), ")")


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
# 返回元素为Point对象的list
def read_csv(filename):
    point_list = []
    csv_file = csv.reader(open(filename))
    for point in csv_file:
        x = float(point[0])
        y = float(point[1])
        new_point = Point(x, y)
        point_list.append(new_point)
    return point_list


# 使用matplotlib库来将点绘制到笛卡尔坐标上
def draw_point(filename):
    point_list = read_csv(filename)
    x = []
    y = []
    for point in point_list:
        x.append(point.get_x())
        y.append(point.get_y())
    plt.scatter(x, y)
    plt.show()


