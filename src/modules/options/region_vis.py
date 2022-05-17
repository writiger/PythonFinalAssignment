import matplotlib
import numpy as np
from src.modules.options.options_panel import show_panel, select_option
import matplotlib.pyplot as plt
from src.modules.tools.specification import divider, starting_liner


def show_region_name(data):
    """ 展示全部地区

    :param data: 处理后的Result类
    :return: None
    """
    for i in data.tables[0].x:
        print(i)
    print('----------------')


def show_line_chart(tit, data, isShow):
    """ 制作折线图

    :param isShow: 是否显示图表
    :param tit: 地区名 用于标题
    :param data: 待制图的数据
    :return: None
    """
    # 准备数据
    langs = np.arange(len(data))
    matplotlib.rc('font', family='KaiTi', weight='bold')
    fig, ax = plt.subplots()

    # 创建图形对象
    plt.plot(langs, data, "b", marker='D', markersize=5, label="人数", color='#6A67CE')
    plt.xlabel("周数", color='#6A67CE')
    plt.ylabel("患病人数", color='#6A67CE')
    plt.title(tit + '患病人数统计表（2014）', fontsize='15', color='#6A67CE')
    plt.legend(loc="lower right")
    for x1, y1 in zip(langs, data):
        plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10, color='#6A67CE')

    # 设置边框颜色
    ax.spines['bottom'].set_color('#947EC3')
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['right'].set_color(None)
    ax.spines['left'].set_color('#B689C0')
    ax.spines['left'].set_linewidth(2)

    plt.grid()
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号
    if isShow:
        plt.show()
    else:
        plt.savefig('../pics/regionByWeek/' + tit + '患病人数统计表（2014）.jpg')
        plt.close()


def show_pie_chart(data, isShow):
    """ 显示饼图

    :param isShow: 是否显示图表
    :param data: 处理数据
    :return: None
    """
    regionNames = data.tables[0].x
    counts = np.zeros([len(regionNames)], dtype=int)
    # 计算总和
    for i in data.tables:
        temp = np.asarray(i.y)
        counts = counts + temp
    allCount = np.sum(counts)
    regionInfo = {
        regionName: count for regionName, count in zip(regionNames, counts)
    }
    # 将患病人数前九汇总
    regionInfo = dict(sorted(regionInfo.items(), key=lambda x: x[1], reverse=True)[:9])
    other = allCount - sum(regionInfo.values())
    regionInfo['Others'] = other

    # 绘制饼状图
    matplotlib.rc('font', family='KaiTi', weight='bold')
    plt.pie(regionInfo.values(), labels=regionInfo.keys(), autopct='%1.2f%%')
    plt.title('患病人数统计表（2014）地区分布', fontsize='15', color='#6A67CE')
    if isShow:
        plt.show()
    else:
        plt.savefig("../pics/regionPie/患病人数统计表（2014）地区分布图.jpg")


def find_region(data, location):
    """ 搜索并返回地区信息

    :param data: 数据集
    :param location: 地区序号
    :return: 仅含有地区相应信息的list
    """
    visData = list()
    for i in data.tables:
        temp = i.y[location]
        visData.append(temp)
    return visData


def show_region_info(data, isShow):
    """ 输入带查询地名，经检测后汇总数据并执行可视化函数

    :param isShow: 是否显示图表
    :param data: 含有地名以及患病数据的数据
    :return : None
    """
    target = input('****请输入待查询地名:')
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
    vis_data = find_region(data, location)
    show_line_chart(target, vis_data, isShow)


def region_classification(data, isShow):
    """ 根据地区将数据分批

    :param isShow: 是否显示
    :param data: 数据集
    :return: None
    """
    starting_liner('Region Classification')
    # 进入选项循环
    while True:
        # 显示功能菜单
        show_panel('level_1_1')
        # 输入选项
        select = select_option('1_1', 3)
        if select == '1_1_1':
            show_region_name(data)
        elif select == '1_1_2':
            show_region_info(data, isShow)
        elif select == '1_1_3':
            show_pie_chart(data, isShow)
        elif select == '1_1_0':
            divider('Quit Region Classification')
            break
