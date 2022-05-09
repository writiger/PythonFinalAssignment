# 处理数据集并打包为对象
import time


class Result:
    """用于存储梳理后的数据"""
    indexUpdatedAt = int
    length = int
    createdAt = int
    category = str
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

    return result
