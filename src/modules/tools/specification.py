# 统一格式

def divider(info):
    """ 打印分割线

    :param info: 分割线信息
    :return: 打印分割线
    """
    print("{:-^50s}".format(info))


def starting_liner(info):
    """ 打印起始行

    :param info: 起始行信息
    :return: 打印起始行
    """
    print("{:*^50s}".format(info))


def select_wrong(info):
    """ 打印错误信息

    :param info: 错误信息
    :return: 打印错误信息
    """
    print('\033[93m' + info + '\033[0m')


def interval():
    """ 功能之间的间隔,便于查看

    :return: 打印一行波浪线
    """
    print("{:~^50s}")

