#导入TensorFlow包
import tensorflow as tf
#TensorFlow程序分为两个阶段：准备阶段和执行阶段

#--------------准备阶段--------------
#定义变量、定义函数、定义操作步骤等，中间隐藏着把变量转化为张量的步骤
#用tf.Variable来定义变量
#注意：定义矩阵的写法([[],[],[]...])
#常数节点 constant node
a = tf.Variable([[2,3]])
b = tf.Variable([[4],[2]])

#矩阵相乘 math multiply
c = tf.matmul(a,b)
print('c----->',c)

#创建用0填充的矩阵
d = tf.zeros([2,4])

#平方
e = tf.square([2])

#平均值
f = tf.reduce_mean([1,3])

#均匀分布的随机数
g = tf.random_uniform([1,10])

#--------------执行阶段--------------
#获取一个能运行TensorFlow的session图，tf.session
#把准备阶段所定义的所有变量都放进session图里进行运行
with tf.Session() as sess:
    #初始化所有的变量
    init = tf.global_variables_initializer()
    sess.run(init)
    #用sess.run获取最终值
    print('a:',a)
    print('a =',sess.run(a))
    print('b =',sess.run(b))
    print('c =',sess.run(c))
    print('d =',sess.run(d))
    print('e =',sess.run(e))
    print('f =',sess.run(f))
    print('g =',sess.run(g))
