from src.modules.options.region_vis import show_line_chart, find_region, show_pie_chart
from src.modules.options.week_vis import show_histogram
from src.modules.tools.specification import divider


def update_week(data):
    """ 更新或加载按星期分类的图表

    :param data: 数据集
    :return: None
    """
    maxWeek = len(data.tables)
    updateNow = 0
    for i in range(maxWeek):
        updateNow += 1
        divider("当前更新至第%d个按星期分类图片" % updateNow)
        show_histogram(str(i + 1), data.tables[i], False)


def update_region(data):
    """ 更新或加载按地区分类的图表

    :param data: 数据集
    :return: None
    """
    regionCnt = len(data.tables[0].x)
    updateNow = 0
    for i in range(regionCnt):
        updateNow += 1
        divider("当前更新至第%d个按地区分类图片" % updateNow)
        show_line_chart(data.tables[0].x[i], find_region(data, i), False)


def update_pie(data):
    """ 更新或加载按地区饼图

    :param data: 数据集
    :return: None
    """
    divider("当前更新地区饼图")
    show_pie_chart(data, False)


def update_pic(data):
    """ 更新或加载所有图表

    :param data: 数据集
    :return: None
    """
    update_region(data)
    update_pie(data)
    update_week(data)
    divider("更新完成")
