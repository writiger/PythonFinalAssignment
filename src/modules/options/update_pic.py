from src.modules.options.region_vis import show_line_chart, find_region, show_pie_chart
from src.modules.options.week_vis import show_histogram
from src.modules.tools.specification import divider, interval


def update_pic(data):
    maxWeek = len(data.tables)
    updateNow = 0
    for i in range(maxWeek):
        updateNow += 1
        divider("当前更新至第%d个图片" % updateNow)
        show_histogram(str(i + 1), data.tables[i], False)
    regionCnt = len(data.tables[0].x)
    for i in range(regionCnt):
        updateNow += 1
        divider("当前更新至第%d个图片" % updateNow)
        show_line_chart(data.tables[0].x[i], find_region(data, i), False)
    divider("当前更新至第%d个图片" % (updateNow + 1))
    show_pie_chart(data, False)
    divider("更新完成")
