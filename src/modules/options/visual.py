import matplotlib
import numpy as np

from src.modules.options.options_panel import show_panel, select_option
import matplotlib.pyplot as plt


def show_histogram(tit, data):
    """ 制作柱状图

    :param tit: 地区名 用于标题
    :param data: 待制图的数据
    :return:
    """
    print('柱状图')
    # 创建图形对象
    print(len(data))
    # 准备数据
    langs = np.arange(len(data))
    # 绘制柱状图
    plt.plot(langs, data, "b", marker='D', markersize=5, label="周活")
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']

    plt.xlabel("周数")
    plt.ylabel("患病人数")
    plt.title(tit+'患病人数统计表（2014）')
    plt.legend(loc="lower right")
    for x1, y1 in zip(langs, data):
        plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)
    plt.show()


def show_region_name(data):
    """ 展示全部地区

    :param data: 处理后的Result类
    :return:
    """
    for i in data.tables[0].x:
        print(i)
    print('----------------')


def show_region_info(data):
    """ 输入带查询地名，经检测后汇总数据并执行可视化函数

    :param data: 含有地名以及患病数据的数据
    """
    target = input('****请输入待查询地名:')
    vis_data = list()
    is_find = False
    location = 0
    # 多组数据地区排序相同随机选择一组查找地区
    # 并记录位置
    for i in data.tables[0].x:
        if i == target:
            is_find = True
            break
        location += 1
    if is_find:
        print('数据集中含有该地名')
    else:
        print('未查询到此地名')
        return
    for i in data.tables:
        temp = i.y[location]
        vis_data.append(temp)
    show_histogram(target, vis_data)


def region_classification(data):
    """ 根据地区将数据分批

    :param data: 数据集
    """
    print('***地区分类***')
    # 进入选项循环
    while True:
        # 显示功能菜单
        show_panel('level_1_1')
        # 输入选项
        select = select_option(1, 2)
        if select == '1_1':
            show_region_name(data)
        elif select == '1_2':
            show_region_info(data)
        elif select == '1_0':
            print('退出地区分类')
            break


def week_classification(data):
    print('星期分类')
    print(data)
