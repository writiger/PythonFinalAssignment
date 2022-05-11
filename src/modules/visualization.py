from src.modules.options.options_panel import Panel, show_panel, select_option
from src.modules.options.region_vis import region_classification
from src.modules.options.week_vis import week_classification
from src.modules.tools.specification import divider, starting_liner


def visualize(data):
    """ 将data数据可视化

    :param data: 可视化数据
    """

    is_stop = False
    starting_liner(' Start of the program ')
    while not is_stop:
        show_panel('level_1')
        select = select_option('0', 2)
        if select == '0_1':
            region_classification(data)
        elif select == '0_2':
            week_classification(data)
        elif select == '0_0':
            divider('End of the program')
            break
