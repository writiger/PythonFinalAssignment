from src.modules.options.options_panel import show_panel, select_option
from src.modules.tools.specification import divider, starting_liner, interval


def show_week_scope(data):
    maxWeek = len(data.tables)
    print('一共含有'+str(maxWeek)+'周')


def show_histogram(data):
    print('histogram')


def show_week_info(data):
    print('show_week_info')


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
