# 处理数据集并打包为对象

class Result:
    """用于存储分析结果"""
    tables = []
    length = int

    def __init__(self):
        self.tables = list()
        self.length = 0

    def __str__(self):
        return "长度为"+str(len(self.tables))+"的Result"

    def append(self, points):
        temp = Points(points.x.copy(), points.y.copy())
        self.length += 1
        self.tables.append(temp)


class Points:
    """用于绘图的坐标"""
    x = list()
    y = list()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        if self.is_match():
            return len(self.x)
        else:
            return 0

    def __str__(self):
        # print(self.y)
        # xStr = 'x轴:'+' '.join(self.x)
        # yStr = 'y轴:'+' '.join(self.y)
        # return xStr+'\n'+yStr
        print(id(self.x))
        print(self.y)
        return ''

    def is_match(self):
        if len(self.x) == len(self.y):
            return True
        else:
            return False


def calculate(data):
    """ 计算某个地区的全年患病总和

    :param data: csv文件中的一行
    :return: 将需要计算的数据相加返回
    """
    ans = 0
    length = len(data)
    for i in range(3, length):
        temp = data[i]
        try:
            ans += int(temp)
        except TypeError:
            pass
            # print('字符串异常')
        except ValueError:
            pass
            # print('字符串异常')
    return ans


def to_numpy(data):
    """ 将数据封装为数组

    :param data: 待拼装数据
    :return: 含有Points列表的Result类
    """
    xList = list()
    yList = list()
    # 用于拆分星期
    weekNow = 1
    result = Result()
    # 删除第一列
    data.pop(0)
    for i in data:
        if str(weekNow) != i[2]:
            points = Points(xList, yList)
            # print("下一组points("+str(weekNow)+")添加points")
            result.append(points)
            weekNow += 1
            xList.clear()
            yList.clear()
            xList.append(i[0])
            yList.append(calculate(i))
        else:
            xList.append(i[0])
            yList.append(calculate(i))

    # print(len(result.tables))
    # for i in result.tables:
    #     print(i.x)
    #     print(i.y)

    return result


def analysis_package(data):
    """ 分析数据集并打包

    :param data: 数据集
    :return: 结果对象
    """

    # print(to_numpy(data))

    return to_numpy(data)
