# 处理数据集并打包为对象
import time
import numpy as np


class Result:
    """用于存储梳理后的数据"""

    indexUpdatedAt = int
    length = int
    createdAt = int
    category = str
    visualData = list()
    owner = {
        "id": str,
        "displayName": str,
        "screenName": str,
        "type": str
    }

    columns = list()

    def __str__(self):
        info = [
            '数据集更新时间\nindexUpdatedAt:' + str(self.indexUpdatedAt),
            '数据集创建时间\ncreatedAt:' + str(self.createdAt),
            '作者id\nowner_id:' + str(self.owner['id']),
            '数据子集个数\ncount:' + str(self.length),
            '数据类型\ncategory:' + str(self.category)
        ]
        return '\n'.join(info)

    def __len__(self):
        return self.length


def address_str(item):
    """  将复杂的address转换为str

    :param item: 数据集中的address
    :return: str
    """
    states = item['human_address'].split(',')
    return states[2].split(':')[1].replace('"', '')


def data_numpy(data):
    """ 将数据格式化为便于可视化的格式

    :param data: 结果字典
    :return: numPy形式的待可视化数据
    """
    drawingData = list()

    for column in data.columns:
        columnList = list()
        for item in column['cachedContents']['top']:
            # point[0]:y  point[1]:x
            point = list()
            point.append(item['count'])
            if isinstance(item['item'], str):
                point.append(item['item'])
            else:
                point.append(address_str(item['item']))
            columnList.append(point)
        drawingData.append(columnList)

    drawingData = np.asarray(drawingData, dtype='O')

    return drawingData


def analysis_package(data):
    """ 分析数据集并打包

    :param data: 数据集
    :return: 结果对象
    """
    result = Result()  # 初始化结果
    result.indexUpdatedAt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['indexUpdatedAt']))  # 读取数据集更新时间
    result.createdAt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['createdAt']))  # 读取数据集创建时间
    result.owner = data['owner']  # 读取数据集作者信息
    result.category = data['category']  # 读取数据集类型
    result.columns = data['columns']  # 读取数据子集
    result.length = len(data['columns'])  # 获取数据子集长度
    result.visualData = data_numpy(result)
    return result
