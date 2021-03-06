#-*- coding: utf-8 -*-

"""
#---------------------------------------------
  filename: ex_runTFvariablescope_pattern.py
  - tf.variable_scope use pattern 1
  Written by Jaewook Kang
  2018 June
#-------------------------------------------
"""
import tensorflow as tf

tf.reset_default_graph()

with tf.variable_scope('test') as scope:
    weights = tf.get_variable(name='weights',
                              shape=[1,2],
                              initializer = tf.random_normal_initializer(mean=0.0,
                                                                         stddev=1.0,
                                                                         dtype=tf.float32))

    scope.reuse_variables()
    weights1 = tf.get_variable(name='weights')

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run([weights, weights1]))
