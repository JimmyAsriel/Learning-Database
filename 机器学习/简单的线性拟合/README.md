## 目的：结合梯度下降算法，来实现自动学习过程。 ##
讨论的模型：**线性回归模型**<br>
给出的数据：期望的Y值，发生的X值<br>
要模拟的数据：根据你模型推测发生x后y的值

	一句话解释:就是用给出的XY求一元一次函数。

## 代码实现逻辑 ##
这里讨论用类似的编程框架来实现一个学习过程。

第一步：节点
----------

给模型中的变量声明。虽然Python是弱类型的语言，但是在Tensorflow的框架下，声明模型的参数值变量就要使用对应的TF对象。

	1.常数节点 constant node
	2.可变节点 Variable
	3.可输入节点 placeholder

> 三种声明一元一次函数的系数部分，常系数


第二步：损失函数
----------

每个模型都有一个损失函数，并且损失值生成函数接受模型公式作为参数。


`loss = tf.reduce_sum(tf.square(linear_model - y))`	
> 损失由预测和期望值之差的和计算
	
1. tf.square() 将输入的 tensor 每一个元素进行平方。
2. tf.reduce_sum() 即对输入的 tensor 进行求和。

`linear_model - y`表达了误差大小	

1. y 代表了理想值。
2. linear_model模型根据(新数据)所判断的y值

第三步：优化器(optimizers)
----------

该类定义了在训练模型的时候添加一个操作的API。常使用子类。 

	Optimizer(父类)
		-GradientDescentOptimizer 梯度下降
		-AdagradOptimizer
		-AdagradDAOptimizer
		-MomentumOptimizer
		-AdamOptimizer
		-FtrlOptimizer
		-RMSPropOptimizer

> 梯度下降算法

第四步：准备训练数据
----------

在这个例子中，数据由浮点数构成。X，Y呈对应关系。

第五步：对所有的变量进行初始化
----------

这一步在逻辑上是不必要的，是对可变参数的初始化。<br>
实际上，初始化是针对Session的，而结点也是针对Session的。

第六步：开始模型训练
----------


Train是误差方程作为参数的优化算法对象。也就是说，优化都是针对误差函数的。误差参数就是模型和期望值的差。

x,y作为参数传入Train中。

第七步：打印参数
----------

获得线性放程的参数。以及总误差，loss放程的总损失量。

注:在这个示例中，假设数据遵循线性方程，得到线性放程linear_model，然后根据linear_model构造误差方程loss，误差方程作为优化器的参数，最后使用