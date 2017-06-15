# Mapping-Analyst
> A graphic tool for visualizing data from wafers

![logo](https://github.com/whyeemcc/Mapping-Analyst/blob/master/images/logo.png)

## 功能：
解析晶圆WAT测试的数据文件，提供可视化的报告和部分统计数据结论。

* 散点图表示晶圆上不同的die的电性参数值
* 晶圆色块图表示不同die的数据值偏差程度
* 自动剔除无效点
* 支持切换同个文件中的不同片wafer数据
* 支持搜索或筛选参数条目
* 支持手动剔除任意die的数据
* 支持数据文件拖拽载入

## 使用的工具及库：
* python 3.6
* PyQt5
* matplotlib 2.0.2
* pyinstaller 