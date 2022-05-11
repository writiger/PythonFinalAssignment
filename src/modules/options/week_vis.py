import matplotlib
import matplotlib.pyplot as plt

from src.modules.options.options_panel import show_panel, select_option
from src.modules.tools.specification import divider, starting_liner, interval, select_wrong


def show_week_scope(data):
    maxWeek = len(data.tables)
    print('一共含有' + str(maxWeek) + '周')


def show_histogram(tit, data):
    y = list(reversed(data.y))
    matplotlib.rc('font', family='SimHei', weight='bold')
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    b = ax.barh(range(len(data.x)), y, color='#6699CC')

    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')

    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(data.x)))
    ax.set_yticklabels(data.x)

    # 不要X横坐标上的label标签。
    plt.xticks(())

    plt.title('第'+tit+'周患病分布图(2014)', loc='center', fontsize='25',
              fontweight='bold', color='red')

    plt.show()



def show_week_info(data):
    target = input('****请输入待查询周数:')
    maxWeek = len(data.tables)
    try:
        select = int(target) - 1
        if select > maxWeek or select < 0:
            select_wrong('请输入正确选项(超出范围)')
            return
        else:
            show_histogram(str(select+1), data.tables[select])
    except TypeError:
        select_wrong('请输入正确选项(TYPE)')
    except ValueError:
        select_wrong('请输入正确选项(VALUE)')


def week_classification(data):
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
            show_week_info(data)
            interval()
        elif select == '1_2_0':
            divider('Quit Week Classification')
            break
