'''

K-means 算法输入为点的集合，K值和迭代次数t（类的个数），输出为K个list
1. 开始时，选取K个点（可以认为随机选取也可以人为指定）作为聚类中心
2. 将点集中每一个点加入离其距离最近的中心的类中
3. 重新计算各类的聚类中心（每个维度简单地求算数平均即可）
4. 重复23步，直到收敛为止

'''

from point import *
import random


# 随机生成一个centroid集合，num为点的总数
def random_centroid(num, k):
    point_set = []
    while len(point_set) < k:
        random_num = random.randint(0, num)
        if random_num not in point_set:
            point_set.append(random_num)
    return point_set


# 第一次随机生成聚类中心
def k_means_random(point_list, k, t):
    num = len(point_list)
    random_list = random_centroid(num, k)
    k_list = []
    for i in random_list:
        k_list.append(point_list[i])
    return k_means(point_list, k_list, t)


# 第一次给定聚类中心
def k_means(point_list, k_list, t):
    cluster_list = cluster(point_list, k_list)
    return k_means_recurse(point_list, cluster_list, t)


def k_means_recurse(point_list, cluster_list, t):
    if t == 0:
        return cluster_list
    centroid_list = []
    for each_cluster in cluster_list:
        centroid = get_centroid(each_cluster)
        centroid_list.append(centroid)
    new_cluster_list = cluster(point_list, centroid_list)
    return k_means_recurse(point_list, new_cluster_list, t-1)


# 计算一个点集的中心
def get_centroid(point_list):
    centroid_x = 0
    centroid_y = 0
    dimension = len(point_list)
    for each_point in point_list:
        centroid_x += each_point.get_x() / dimension
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
            current_dis = distance_between_points(each_point, centroid_list[i])
            if current_dis < min_dis:
                min_dis = current_dis
                min_index = i
        cluster_list[min_index].append(each_point)
    return cluster_list


if __name__ == '__main__':
    # a = Point(1, 2)
    # b = Point(2, 2)
    # pl = []
    # pl.append(a)
    # pl.append(b)
    # c = get_centroid(pl)
    # c.prn()
    lis = random_centroid(10, 4)
    print(lis)
