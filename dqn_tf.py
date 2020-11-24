import os
import numpy as np
import tensorflow as tf

class DeepQNetwork(object):
    def __init__(self, lr, n_actions, name, fcl_dims=256,
            input_dims=(210,160,4), chkpt_dir='tmp/dqn'):
        selfl.lr = lr
        self.name = name
        self.n_anctions = n_actions
        self.fcl_dims = fcl_dims
        self.input_dims = input_dims
        self.sess = tensorflow.Session()
        self.build_nutwork()
        self.sess.run(tf.global_variables_initializer())
        self.saver = tf.train.Saver()
        self.checkpoint_file = os.path.join(chkpt_dir, 'deepqnet.ckpt')
        self.params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.name)


    def build_net(self):
        with tf.variable_scope(self.name):
            self.input = tf.placeholder(tf.float32, shape=[None, *self_input_dims], name='inputs')
            self.action = tf.placeholder(tf.float32, shape[None, self.n_actions], name='action_taken')
            self.q_target = tf.placeholder(tf.float32, shape=[None, self.n_actions])
            
            conv1 = tf.layers.conv2d(input=self, input, filters=32, kernel_size=(8, 8), strides=4,
                    name='conv1', kernel_initializer=tf.variance_scaling_initializer(scale=2))
            conv1_activated = tf.nn.relu(conv1)

            conv2 = tf.layers.conv2d(inputs=conv1_activated, filters=64,  
