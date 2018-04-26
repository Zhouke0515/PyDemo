import tensorflow as tf


def demo1():
    # 定义一个常量Tensor
    t1 = tf.constant([[2, 3]])
    t2 = tf.constant([[4], [7]])
    # 定义一个matmul Op，Tensoflow中任何Op都返回Tensor
    product = tf.matmul(t1, t2)  #矩阵乘法
    print(product)
    # 定义一个会话，使用默认图
    with tf.Session() as sess:
        # 会话执行图中的Op
        result = sess.run(product)
        print(result)


def demo2():
    # 定义一个变量
    count = tf.Variable(0)
    new_value = tf.add(count, 1)
    # 定义一个赋值Op
    count_assign = tf.assign(count, new_value)
    # 使用变量，必须进行初始化
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for i in range(5):
            sess.run(count_assign)
            print(sess.run(count))


if __name__ == '__main__':
    demo2()
