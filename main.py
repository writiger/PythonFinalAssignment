from src.modules.load_csv import load_csv
from src.modules.analysis_package import analysis_package
from src.modules.visualization import visualize

if __name__ == '__main__':
    dataSet = load_csv('resource/nndss-table-ii.-mumps-to-rabies-animal.csv')  # 从csv中读取数据
    anaResult = analysis_package(dataSet)  # 分析数据并打包
    visualize(anaResult)  # 数据可视化

