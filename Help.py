class Help:
    about = '''
载入：
可从菜单打开文件，亦支持直接拖拽 Mapping 数据文件到主界面。
    
WaferID：
代表 Wafer 的编号，当一个文件中包含多片 wafer 的数据时，可在下拉列表中选择进行切换。

筛选：
搜索框中输入关键字进行搜索，筛选出包含该关键字的全部 Item 以重新显示。

显示：
图形显示区域上方部分的控件可进行拖动、放大、自定义坐标轴显示范围等功能。

统计：
1，数据为 '+3.000000E+30' 的值定义为坏点，做一维数据统计前，会自动剔除。

2，为保证原始数据的完整性，除坏点外，默认状态下不会对数据中 3σ 以外\
的点进行循环筛除，并使用 die 数值偏离 Median 值的百分比(delta)来定义：
δ(x)=abs((x-median)/median)。

3，打开循环筛除 3σ 以外点的开关后，会自动筛除距离 Median 值 3σ 以\
外的 die，循环计算，直至所有数值都在 3σ 以内为止。

3，提供手动剔除指定 die 的功能，剔除后，所有的统计数据及图形会重新刷新。\
点击重置按钮即可恢复初始的所有 die。

声明：
该软件只提供对 RawData 进行 review 的功能，若要输出整个数据的统计概要，请\
使用 YanQing 的 Watex 工具。


如有Bug，请联系：
Author: Grothendieck_Yu
Mail: whyeemcc@gmail.com
'''