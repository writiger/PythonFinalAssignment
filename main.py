from src.modules.load_json import load_json
from src.modules.analysis_package import analysis_package, Result
from src.modules.visualization import vis

if __name__ == '__main__':
    dataSet = load_json('resource/socrata_metadata_nndss-table-ii.-mumps-to-rabies-animal.json')  # 从json中读取数据
    anaResult = analysis_package(dataSet)  # 分析数据并打包
    vis(anaResult)  # 数据可视化

