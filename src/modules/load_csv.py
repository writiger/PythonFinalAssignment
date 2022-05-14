import json
import csv


def load_csv(location):
    """ 从csv文件中读取数据集转换为字典

    :param location: 待分析数据集相对位置
    :return: 完整的字典格式数据
    """
    data = list()
    with open(location) as f:
        reader = csv.reader(f)
        for row in reader:
            # 行号从1开始
            data.append(row)
    return data

