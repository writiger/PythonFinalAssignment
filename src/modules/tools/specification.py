# 统一格式

def divider(info):
    print("{:-^50s}".format(info))


def starting_liner(info):
    print("{:*^50s}".format(info))


def select_wrong(info):
    print('\033[93m' + info + '\033[0m')
