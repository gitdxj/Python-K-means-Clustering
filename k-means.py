'''

K-means 算法输入为点的集合，K值和迭代次数t（类的个数），输出为K个list
1. 开始时，选取K个点（可以认为随机选取也可以人为指定）作为聚类中心
2. 将点集中每一个点加入离其距离最近的中心的类中
3. 重新计算各类的聚类中心（每个维度简单地求算数平均即可）
4. 重复23步，直到收敛为止

'''

from point import *
import random
import matplotlib.pyplot as plt


# 随机生成一个centroid集合，num为点的总数
def random_centroid(num, k):
    point_set = []
    while len(point_set) < k:
        random_num = random.randint(0, num-1)  # 在0到num-1之间随机选择一个数
        if random_num not in point_set:  # 如果集合里还没有这个数字就添加进去
            point_set.append(random_num)
    return point_set


# 随机生成聚类中心
def k_means_random(point_list, k, t):
    num = len(point_list)
    random_list = random_centroid(num, k)  # 随机找出k个点
    k_list = []
    for i in random_list:
        k_list.append(point_list[i])
    print("初始点为：")
    for each in k_list:
        each.prn()
    return k_means(point_list, k_list, t)


# 给定聚类中心
def k_means(point_list, k_list, t):
    cluster_list = cluster(point_list, k_list)
    return k_means_recurse(point_list, cluster_list, t)


# 下面这个函数是算法执行过程中不断迭代的部分
# 根据上一次聚类的结果计算新的centroid
# 然后重新划分
def k_means_recurse(point_list, cluster_list, t):  # t为迭代次数
    print("现在t为： " + str(t))
    if t == 0:  # 迭代次数用尽就结束
        return cluster_list
    centroid_list = []
    for each_cluster in cluster_list:
        centroid = get_centroid(each_cluster)
        centroid_list.append(centroid)
    new_cluster_list = cluster(point_list, centroid_list)
    if new_cluster_list == cluster_list:  # 如果聚类结果和上一次聚类的结果相同，说明已经收敛
        print("提前收敛， t为： " + str(t))
        return new_cluster_list
    return k_means_recurse(point_list, new_cluster_list, t-1)


# 计算一个点集的中心（简单地求各个维度的平均值）
def get_centroid(point_list):
    centroid_x = 0
    centroid_y = 0
    dimension = len(point_list)
    for each_point in point_list:
        centroid_x += each_point.get_x() / dimension  # 算数平均
        centroid_y += each_point.get_y() / dimension
    centroid = Point(centroid_x, centroid_y)
    return centroid


# 根据聚类中心分配点集中每一个点
# 计算每一个点到个中心的距离，分配给距离最近的那个类
# 要注意聚类中心并不是一个实际的点
def cluster(point_list, centroid_list):
    k = len(centroid_list)
    cluster_list = []
    for i in range(k):
        cluster_list.append([])
    for each_point in point_list:
        min_dis = distance_between_points(each_point, centroid_list[0])
        min_index = 0
        for i in range(1, len(centroid_list)):
            current_dis = distance_between_points(each_point, centroid_list[i])  # 计算该点到每一个centroid的距离
            if current_dis < min_dis:  # 如果算出的距离小于当前记录的最小距离
                min_dis = current_dis
                min_index = i
        cluster_list[min_index].append(each_point)  # 把此点归入与其最近的centroid代表的类里
    return cluster_list


# filename为文件名， k为类的数目， t为迭代次数
def draw_cluster(filename, k, t):
    color_set = ['r', 'y', 'b', 'k']  # matplotlib中描述点颜色的参数
    if k > 4:
        print("颜色不够用了！请设置小一点的k")
    else:
        x = []
        y = []
        point_list = read_csv(filename)
        clus = k_means_random(point_list, k, t)
        for i in range(len(clus)):  # 第i个类
            xi = []  # Xi是第i个类里的点横坐标的集合
            yi = []  # Yi是第i个类里的点纵坐标的集合
            for each in clus[i]:
                xi.append(each.get_x())
                yi.append(each.get_y())
            x.append(xi)
            y.append(yi)
        for i in range(k):
            plt.scatter(x[i], y[i], 20, color_set[i])
        plt.show()


if __name__ == '__main__':
    # draw_point("data.csv")
    draw_cluster("data.csv", 3, 20)
