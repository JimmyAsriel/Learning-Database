import tensorflow as tf
#数学库
import numpy as np
#绘制图像的库
import matplotlib.pyplot as plt

# Model parameters，可变节点 Variable
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output，可输入节点 placeholder
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss 损失函数
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer 优化器对象，该对象的子类GradientDescentOptimizer梯度下降
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = np.array([ 0.07786339,-0.03961813, 0.01103904,-0.04069594, -0.03422907,0.00564998,0.08864151,-0.03315126,-0.05686312, -0.03099563,0.05522933,-0.06009656,0.00133873,-0.02345095, -0.07410811,0.01966154,-0.01590626,-0.01590626,0.03906215, -0.0730303 ])

y_train = np.array([ 233., 91., 111., 152., 120., 67., 310., 94., 183., 66., 173., 72., 49., 64., 48., 178., 104., 132., 220., 57.])

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init) # reset values to wrong
for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})
    # evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

#-------------plot the result--------------------
plt.scatter(x_train,y_train)
y = curr_W[0] * x_train + curr_b[0]
plt.plot(x_train, y, color='red')
plt.show()
