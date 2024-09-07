#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :3D_drought_2.py
@说明        :
@时间        :2024/09/01 12:04:53
@作者        :YZQ
'''


import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


def plot_cube(x_ranges, y_ranges, z_values, colors, alphas, MatrixSize):
    """
    绘制三维立方体中的部分立方体

    参数：
    - x_ranges: 每个月份在x轴范围的字典,如 {3: (0, 4), 6: (5, 9), 9: (10, 14)}
    - y_ranges: 每个月份在y轴范围的字典,如 {3: (0, 4), 6: (5, 9), 9: (10, 14)}
    - z_values: z轴上的特定月份列表,例如 [3, 6, 9]
    - colors: 每个z_value的颜色字典,例如 {3: 'blue', 6: 'green', 9: 'red'}
    - alphas: 每个z_value的透明度字典,例如 {3: 0.5, 6: 0.5, 9: 0.5}
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制需要展示的部分
    for z in z_values:
        x_range = x_ranges[z]
        y_range = y_ranges[z]

        # 绘制未展示部分的立方体线框
        for x in range(3, MatrixSize - 2):
            for y in range(2, MatrixSize - 2):
                if not (x_range[0] <= x < x_range[1] and y_range[0] <= y < y_range[1]):
                    vertices2 = [
                        [x, y, z - 1], [x + 1, y, z - 1], [x + 1, y + 1, z - 1], [x, y + 1, z - 1],
                        [x, y, z], [x + 1, y, z], [x + 1, y + 1, z], [x, y + 1, z]
                    ]
                    # 定义每个立方体的面
                    faces2 = [
                        [vertices2[0], vertices2[1], vertices2[2], vertices2[3]],
                        [vertices2[4], vertices2[5], vertices2[6], vertices2[7]],
                        [vertices2[0], vertices2[1], vertices2[5], vertices2[4]],
                        [vertices2[2], vertices2[3], vertices2[7], vertices2[6]],
                        [vertices2[1], vertices2[2], vertices2[6], vertices2[5]],
                        [vertices2[4], vertices2[7], vertices2[3], vertices2[0]]
                    ]

                    # 绘制立方体的面,应用颜色和透明度
                    ax.add_collection3d(Poly3DCollection(
                        faces2,
                        facecolors='whitesmoke',  # 非干旱区背景颜色
                        linewidths=0.2,
                        edgecolors=None,
                        alpha=alphas[z]
                    ))

        # 绘制干旱区域的立方体
        for x in range(*x_range):
            for y in range(*y_range):
                # 创建立方体顶点
                vertices = [
                    [x, y, z - 1], [x + 1, y, z - 1], [x + 1, y + 1, z - 1], [x, y + 1, z - 1],
                    [x, y, z], [x + 1, y, z], [x + 1, y + 1, z], [x, y + 1, z]
                ]
                # 定义每个立方体的面
                faces = [
                    [vertices[0], vertices[1], vertices[2], vertices[3]],
                    [vertices[4], vertices[5], vertices[6], vertices[7]],
                    [vertices[0], vertices[1], vertices[5], vertices[4]],
                    [vertices[2], vertices[3], vertices[7], vertices[6]],
                    [vertices[1], vertices[2], vertices[6], vertices[5]],
                    [vertices[4], vertices[7], vertices[3], vertices[0]]
                ]
                # 绘制立方体的面,应用颜色和透明度
                ax.add_collection3d(Poly3DCollection(
                    faces,
                    facecolors=colors[z],
                    linewidths=0.1,
                    edgecolors='lightgrey',
                    alpha=alphas[z]
                ))

        # 绘制干旱区域的立方体
        for x in range(*(10, 20)):
            for y in range(*(10, 20)):
                # 创建立方体顶点
                vertices3 = [
                    [x, y, z - 1], [x + 1, y, z - 1], [x + 1, y + 1, z - 1], [x, y + 1, z - 1],
                    [x, y, z], [x + 1, y, z], [x + 1, y + 1, z], [x, y + 1, z]
                ]
                # 定义每个立方体的面
                faces3 = [
                    [vertices3[0], vertices3[1], vertices3[2], vertices3[3]],
                    [vertices3[4], vertices3[5], vertices3[6], vertices3[7]],
                    [vertices3[0], vertices3[1], vertices3[5], vertices3[4]],
                    [vertices3[2], vertices3[3], vertices3[7], vertices3[6]],
                    [vertices3[1], vertices3[2], vertices3[6], vertices3[5]],
                    [vertices3[4], vertices3[7], vertices3[3], vertices3[0]]
                ]
                # 绘制立方体的面,应用颜色和透明度
                ax.add_collection3d(Poly3DCollection(
                    faces3,
                    facecolors='red',
                    linewidths=0.1,
                    edgecolors='lightgrey',
                    alpha=alphas[z]
                ))

    # 设置坐标轴的范围
    ax.set_xlim(0, MatrixSize)
    ax.set_ylim(0, MatrixSize)
    ax.set_zlim(0, MatrixSize)

    # 去除灰色背景和网格
    # ax.set_facecolor('white')
    # ax.grid(False)
    # ax.set_box_aspect([1, 1, 1])

    # 隐藏三维轴的灰色背景框和边框线
    ax.xaxis.pane.set_visible(False)  # 隐藏X轴的背景
    ax.yaxis.pane.set_visible(False)  # 隐藏Y轴的背景
    ax.zaxis.pane.set_visible(False)  # 隐藏Z轴的背景

    '''
    进一步修改
    '''
    # Plot figure
    # 支持中文
    mpl.rcParams['font.sans-serif'] = [u'SimHei']  # 中文字体可修改
    mpl.rcParams['axes.unicode_minus'] = False

    # 添加X, Y, Z轴的方向箭头,起点与坐标轴一致,颜色为黑色
    # 箭头的长度
    arrow_length = MatrixSize
    # quiver(000 000) 前面3个是起点 后面3个箭头指向的终点
    ax.quiver(0, arrow_length, 0, arrow_length + 3, 0, 0, color='black', arrow_length_ratio=0.1)  # X轴箭头
    ax.quiver(0, arrow_length, 0, 0, -arrow_length - 6, 0, color='black', arrow_length_ratio=0.1)  # Y轴箭头
    ax.quiver(0, arrow_length, 0, 0, 0, arrow_length, color='black', arrow_length_ratio=0.1)  # Z轴箭头

    # # 设置X,Y轴的标签
    # ax.set_xlabel('经度(Lon)')
    # ax.set_ylabel('纬度(Lat)')
    # ax.set_zlabel('时间(t)')

    # 隐藏最外层的刻度线及标记
    ax.xaxis.line.set_lw(0.0)  # 隐藏X轴的线条
    ax.yaxis.line.set_lw(0.0)  # 隐藏Y轴的线条
    ax.zaxis.line.set_lw(0.0)  # 隐藏Z轴的线条

    # 隐藏全部刻度线
    ax.xaxis.set_ticks([])  # 隐藏X轴的刻度线
    ax.yaxis.set_ticks([])  # 隐藏Y轴的刻度线
    ax.zaxis.set_ticks([])  # 隐藏Z轴

    # # 设置图的标题
    # plt.title('3D Drought')

    # 视角设置 view_init(elev, azim) 'elev' 存储 z 平面中的仰角 、‘azim’ 存储 x,y 平面中的方位角
    ax.view_init(9, -78)

    # 显示绘图
    plt.show()


if __name__ == '__main__':
    # 设定参数
    # 显示的
    month1 = 2
    month2 = 12
    month3 = 22

    x_ranges = {month1: (5, 20), month2: (6, 25), month3: (9, 25)}
    y_ranges = {month1: (5, 20), month2: (6, 25), month3: (9, 25)}
    z_values = [month1, month2, month3]  # 显示的月份

    colors = {month1: 'bisque', month2: 'brown', month3: 'tan'}  # 各月份的颜色
    alphas = {month1: 1, month2: 1, month3: 1}  # 各月份的透明度

    # # 整体立方体的大小
    # MatrixSize = 30

    # 绘制立方体
    plot_cube(x_ranges, y_ranges, z_values, colors, alphas, MatrixSize=30)
