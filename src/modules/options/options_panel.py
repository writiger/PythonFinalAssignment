# 操作选项

def show_panel(level):
    """

    :param level: 待显示面板
    :return:
    """
    panel = Panel()
    panel.show(level)


def select_option(level, maxOption):
    """ 将选项返回

    :param level: 当前面板
    :param maxOption: 选项数字最大值
    :return: 选项
    """
    select = input('')
    try:
        select = int(select)
        if select > maxOption or select < 0:
            print('请输入正确选项(超出范围)')
            return '0'
        else:
            return str(level) + '_' + str(select)  # 格式为*_*
    except TypeError:
        print('请输入正确选项(TYPE)')
    except ValueError:
        print('请输入正确选项(VALUE)')


class Panel:
    """选项面板展示"""
    options = dict()

    def __init__(self):
        self.options = {
            'level_1': [
                '0.退出',
                '1.地区分类',
                '2.星期分类'
            ],
            'level_1_1': [
                '0.返回上一级',
                '1.显示所有地区',
                '2.选择地区'
            ],
            'level_1_2': [
                '0.返回上一级',
                '1.查询星期范围',
                '2.选择星期'
            ]
        }

    def show(self, level):
        """

        :param level: 面板层级
        """
        for i in self.options[level]:
            print(i)