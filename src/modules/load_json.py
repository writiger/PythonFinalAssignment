import json


def load_json(location):
    """ 从json文件中读取数据集转换为字典

    :param location: 待分析数据集相对位置
    :return: 完整的字典格式数据
    """
    with open(location, 'r') as fp:
        json_data = json.load(fp)
    return json_data

