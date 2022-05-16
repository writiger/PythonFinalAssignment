import matplotlib
import matplotlib.pyplot as plt

from src.modules.options.options_panel import show_panel, select_option
from src.modules.tools.specification import divider, starting_liner, interval, select_wrong


def show_week_scope(data):
    """ 输出星期总数

    :param data: 数据集
    :return: None
    """
    maxWeek = len(data.tables)
    print('一共含有' + str(maxWeek) + '周')


def show_histogram(tit, data, isShow):
    """

    :param tit: 可视化标题
    :param data: 可视化数据
    :param isShow: 是否显示图表
    :return:
    """
    y = list(reversed(data.y))
    matplotlib.rc('font', family='KaiTi', weight='bold')
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots(figsize=(10, 12))
    b = ax.barh(range(len(data.x)), y, color='#6A67CE')

    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')

    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(data.x)))
    # 调整y轴坐标顺序
    data.x.reverse()
    ax.set_yticklabels(data.x, fontsize='8')
    # 设置图表边框颜色
    ax.spines['bottom'].set_color('#947EC3')
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_color('#947EC3')
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_color(None)
    ax.spines['left'].set_color('#B689C0')
    ax.spines['left'].set_linewidth(2)

    plt.title('第' + tit + '周患病分布图(2014)', loc='center', fontsize='15', color='#6A67CE')
    if isShow:
        plt.show()

    plt.savefig("../pics/week/第" + tit + "周患病分布图(2014).jpg")
    plt.clf()
    plt.close()


def show_week_info(data, isShow):
    """

    :param data: 带展示数据
    :param isShow: 是否显示图表
    :return:
    """
    target = input('****请输入待查询周数:')
    maxWeek = len(data.tables)
    try:
        select = int(target) - 1
        if select > maxWeek or select < 0:
            select_wrong('请输入正确选项(超出范围)')
            return
        else:
            show_histogram(str(select + 1), data.tables[select], isShow)
    except TypeError:
        select_wrong('请输入正确选项(TYPE)')
    except ValueError:
        select_wrong('请输入正确选项(VALUE)')


def week_classification(data):
    """ 显示面板并选择功能

    :param data: 数据集
    :return: None
    """
    starting_liner('Week Classification')
    # 进入选项循环
    while True:
        # 显示功能菜单
        show_panel('level_1_2')
        # 输入选项
        select = select_option('1_2', 2)
        if select == '1_2_1':
            show_week_scope(data)
            interval()
        elif select == '1_2_2':
            show_week_info(data, True)
            interval()
        elif select == '1_2_0':
            divider('Quit Week Classification')
            break
