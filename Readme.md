# PythonFinalAssignment

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [示例](#示例)
- [相关仓库](#相关仓库)
- [项目结构 ](#项目结构)
## 背景
python课程大作业,基于matplotlib库的数据可视化  
数据来源 [阿里云天池数据集](https://tianchi.aliyun.com/?spm=5176.12282013.J_3941670930.2.180d13deZMBtbf)
[NNDSS - Mumps to Rabies, animal NNDSS-狂犬病流行性腮腺炎](https://tianchi.aliyun.com/dataset/dataDetail?dataId=90774)

## 安装

这个项目使用 [numpy](https://numpy.org/) 和 [matplotlib](https://matplotlib.org/)。请确保你本地安装了它们。

```sh
$  pip install numpy
$  pip install matplotlib
```

所需文件夹**程序会尝试自动生成**
```shell
../pics/regionByWeek
../pics/regionPie
../pics/week
```
## 使用说明

这是一个通过**特定格式**csv格式的表格显示或保存图表的python程序  

```sh
$ python main.py
```


## 示例

```shell
	************** Start of the program **************
0.退出
1.地区分类
2.星期分类
3.更新图片
请输入所选功能:
```

```shell
	**************Region Classification***************
0.返回上一级
1.显示所有地区
2.选择地区
3.生成地区饼图
请输入所选功能:
```

```shell
	***************Week Classification****************
0.返回上一级
1.查询星期范围
2.选择星期
请输入所选功能:
```

```shell
-----------------当前更新至第1个按星期分类图片------------------
-----------------当前更新至第2个按星期分类图片------------------
-----------------当前更新至第3个按星期分类图片------------------
-----------------当前更新至第4个按星期分类图片------------------
-----------------当前更新至第5个按星期分类图片------------------
-----------------当前更新至第6个按星期分类图片------------------
-----------------当前更新至第7个按星期分类图片------------------
		 ...
```

![这是一个结果](https://test-resource-1310107767.cos.ap-nanjing.myqcloud.com/%E6%82%A3%E7%97%85%E4%BA%BA%E6%95%B0%E7%BB%9F%E8%AE%A1%E8%A1%A8%EF%BC%882014%EF%BC%89%E5%9C%B0%E5%8C%BA%E5%88%86%E5%B8%83%E5%9B%BE.jpg "2014")

## 项目结构
> +--.gitignore  
+--main.py    
+--Readme.md  
+--resource  
| +--nndss-table-ii.-mumps-to-rabies-animal.csv  
+--src  
| +--modules  
| | +--analysis_package.py   
| | +--load_csv.py   
| | +--options  
| | | +--options_panel.py  
| | | +--region_vis.py  
| | | +--update_pic.py  
| | | +--week_vis.py  
| | +--tools  
| | | +--init_dir.py  
| | | +--specification.py  
| | +--visualization.py  

## 相关仓库

- [NumPy](https://github.com/numpy/numpy) — NumPy is the fundamental package for scientific computing with Python.
- [matplotlib](https://github.com/matplotlib/matplotlib) — Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.


