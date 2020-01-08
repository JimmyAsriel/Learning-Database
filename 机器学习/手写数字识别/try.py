import tensorflow as tf
import numpy
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as sess:
    # add this line to use TensorBoard.
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print (sess.run(x))
writer.close() # close the writer when you’re done using it