import os


def ini_dir():
    """ 创建文件夹

    :return: None
    """
    paths = [
        '../pics',
        '../pics/regionByWeek',
        '../pics/regionPie',
        '../pics/week'
    ]
    try:
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
    except OSError as error:
        print(error)
