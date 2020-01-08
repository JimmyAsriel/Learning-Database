import tensorflow as tf
import input_data
import numpy
mnist = input_data.read_data_sets("Mnist/", one_hot=True)
# 一个one-hot向量除了某一位的数字是1以外其余各维度数字都是0

# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.4 # 占用GPU40%的显存
# session = tf.Session(config=config)
sess = tf.InteractiveSession()

x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    # 截断正态分布(shape,平均值mean,标准差stddev)
    # 返回值与平均值差距不会超过标准差的2倍
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)  # 加入噪声，初始化偏置项
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')  # return a tensor(called feature map)
# 第一个参数input，有形状[训练时一个batch的图片数量, 图片高度, 图片宽度, 图像通道数]
# 调用时为[-1, 28, 28, 1]
# 第二个参数卷积核，有形状[卷积核的高度，卷积核的宽度，图像通道数，卷积核个数]
# 调用时为[5, 5, 1, 32] （得到32个feature map）
# 第三个参数strides：卷积时在图像每一维的步长，是一个一维的向量，长度为4(一般首末为1)
# 第四个参数padding：string类型的量，只能是"SAME","VALID"其中之一，决定了不同的卷积方式
# VALID只能匹配内部像素；而SAME可以在图像外部补0,从而做到只要图像中的一个像素就可以和卷积核做卷积操作,而VALID不行


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# 第一个参数value输入通常是feature map，有形状[batch, height, width, channels]
# 第二个参数ksize：池化窗口的大小（一个四维向量），一般是[1, height, width, 1]，因为我们不想在batch和channels上做池化，所以这两个维度设为了1
# 第三个参数strides：和卷积类似，窗口在每一个维度上滑动的步长，一般也是[1, stride, stride, 1]
# 第四个参数padding：和卷积类似，可以取'VALID' 或者'SAME'
# 返回一个Tensor，类型不变，shape仍然是[batch, height, width, channels]这种形式


# 第一层卷积，每5*5的patch得到32个特征
W_conv1 = weight_variable([5, 5, 1, 32])  # 卷积核[patch大小a,patch大小b,输入通道,输出通道（卷积核个数）]
b_conv1 = bias_variable([32])
x_image = tf.reshape(x, [-1, 28, 28, 1])   # -1是缺省值，先满足其他几个参数的要求
# [,宽,高,颜色通道（灰度为1，彩色为3）]   x的形状是[None, 784]; None*784=(-1)*28*28*1

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # 用relu进行整流
# 返回tensor: [batch, height, width, channels]，即[?, 28, 28, 32]
# 如果padding='VALID'，那么为24*24，详见shape.jpg
h_pool1 = max_pool_2x2(h_conv1)  # 池化
# [?, 14, 14, 32]

# 第二层卷积，每5*5的patch得到64个特征
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# [?, 14, 14, 64]
h_pool2 = max_pool_2x2(h_conv2)
# [?, 7, 7, 64]

# 密集连接层
W_fc1 = weight_variable([7*7*64, 1024])  # 图片尺寸减小为7*7，加入1024个神经元的全连接层
# 28*28 ->(conv 5*5) 32@28*28 ->(pool 2*2) 32@14*14 ->(conv 5*5) 64@14*14 ->(pool) 64@7*7
# [?, 28, 28, 1] -> [?, 7, 7, 64]
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
# [?, 7, 7, 64] -> [?, 7*7*64]
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
# [?, 7*7*64] -> [?, 1024]

# Dropout以减少过拟合
keep_prob = tf.placeholder("float")   # 训练时指定
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 训练和评估
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
writer = tf.summary.FileWriter('D:\ITstudy\机器学习\CNN\my_graph', sess.graph)
sess.run(tf.initialize_all_variables())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g%%" % (i, 100*train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g" % accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

sess.close()