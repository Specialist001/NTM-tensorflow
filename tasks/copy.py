from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from random import randint

from layers import *

print_interval = 10
min_length = 1
max_length = 20

def generate_sequence(length, bits):
    seq = np.zeros([length, 1, bits + 2])
    for idx in xrange(length):
        seq[idx, :, 2:bits+2] = np.random.rand(bits).round()
    return seq

def task_forward(model, seq, config, print_flag, start_symbol, end_symbol):
    seq_length = len(seq)
    loss = 0

    # start symobl
    model.forward(start_symbol)

    if print_flag: print('write head max')

    for idx in xrange(seq_length):
        x = model.forward(seq[idx])
        if print_flag: model.print_write_max()

    # end symbol
    model.forward(end_symbol)

    zeros = tf.zeros(config.input_dim)
    output = tf.zeros([seq_length, config.input_dim])

    if print_flag: print('read head max')

    for idx in xrange(req_length):
        pass

def task(model, config):
    print("epoch = %s" % config.epoch)
    print("learning rate= %s" % config.lr_rate)
    print("momentum = %s" % config.momentum)
    print("decay = %s" % config.decay)

    start_symbol = np.zeros([1, config.input_dim])
    start_symbol[0][1] = 1
    end_symbol = np.zeros([1, config.input_dim])
    end_symbol[0][2] = 1

    for idx in xrange(config.epoch):
        print_flag = (idx % print_interval == 0)
        loss = 0

        seq_length = randint(min_length, max_length)
        seq = generate_sequence(seq_length, config.input_dim - 2)
        output, train, sample_loss = task_forward(model, seq, config, print_flag, start_symbol, end_symbol)
        loss = sample_loss

        if print_flag:
            print("target:")
            print(seq)
            print("output:")
            print(output)