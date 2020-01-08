# 这是什么? #
数据分析以及机器学习。

**数据分析与数据挖掘**
    数据分析主要实现三大作用
    现状分析、原因分析、预测分析
    方法：以各种统计方法为主
    
**数据挖掘侧重解决四类问题**
    分类、聚类、关联、预测
    方法：决策树、神经网络、关联规则、聚类分析
    等统计学方法和人工智能、机器学习的方法

> 注：项目的每个例子以单独的目录存放，方便所需阅读
## 环境 ##
虽然Anaconda的最佳用法是应该使用命令行配置环境并导出自己的实验环境方便运行的，但是原因在于注意力更多在Tensorflow的学习，故最大限度的方便Windows安装了。(不折腾)

> 实验并不一定仅仅使用TensorFlow框架，它可能是依赖不同的类库工具。

> 考虑到这是为了学习模型思想为目的，实验的数据规模被控制了。

- Windows10
- Pycharm
- Anaconda
    预装了大量常用 Packages。
    完全开源和免费。
    额外的加速和优化是收费的，但对于学术用途，可以申请免费的 License。
    对全平台和几乎所有Python版本支持。

## 安装配置过程 ##
> 过程根据Windows为准

1. 安装Pycharm，Pycharm是先进的PythonIDE，今后它作为主要的窗体来编写调试code。

	打开Pycharm，上侧任务栏点击，File，Setting，Project Interpreter，Setting，Add local。

	Path的目录为 
	> 例:E:\Anaconda\ens\tensorflow\python.exe
2. 安装Anaconda，开源Py环境管理软件。

	安装完毕后，通过Anacoda Navigator进入，可以从左侧的菜单中看到HOME菜单，默认情况下会有Tensorflow的运行虚拟环境。点击该环境，安装并升级所有的模块。

