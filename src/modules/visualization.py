from src.modules.options.options_panel import Panel, show_panel, select_option
from src.modules.options.visual import region_classification, week_classification


def visualize(data):
    """ 将data数据可视化

    :param data: 可视化数据
    """

    is_stop = False
    while not is_stop:
        show_panel('level_1')
        select = select_option(0, 2)
        if select == '0_1':
            region_classification(data)
        elif select == '0_2':
            week_classification(data)
        elif select == '0_0':
            print('程序退出')
            break
